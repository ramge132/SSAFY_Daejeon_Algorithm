from collections import deque
# 상 우 하 좌
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# 회전 시킨 후 획득 가능한 유물 개수
def canGet(matrix_for_find, explore_list, position, rotating_degree, after_rotating=True):
    # 최종 가져올 유물들
    visited = [[False]*5 for _ in range(5)]
    count = 0

    # bfs 돌릴 좌표들 하나씩 큐에 담고 bfs
    for x, y in explore_list:
        # 한 bfs당 유물들 임시 방문처리
        temp_visited = [[False]*5 for _ in range(5)]
        temp_visited[y][x] = True
        queue = deque([(x, y)])
        temp_cnt = 1
        while queue:
            cx, cy = queue.popleft()

            for dx, dy in dxy:
                nx, ny = cx + dx, cy + dy

                # 다음 좌표가 범위를 넘어간 경우
                if not (0 <= nx <= 4 and 0 <= ny <= 4):
                    continue

                # 이미 방문한 경우
                # 자신의 값과 다른 경우
                if visited[ny][nx] or temp_visited[ny][nx] or matrix_for_find[ny][nx] != matrix_for_find[cy][cx]:
                    continue

                # 방문하지 않고 자신과 값이 같다면 추가
                else:
                    queue.append((nx, ny))
                    temp_visited[ny][nx] = True
                    temp_cnt += 1
        
        # 연결된 유물이 3개 이상인 경우
        if temp_cnt >= 3:
            count += temp_cnt
            visited = [[visited[j][i] or temp_visited[j][i] for i in range(5)] for j in range(5)]

    return count, position, rotating_degree, visited


# 중심 좌표를 지정 해당 좌표를 중심으로 3*3 회전
def rotate(position, rotating_degree):
    temp_matrix = [a[:] for a in matrix]
    explore_list = set()

    # 돌려야 하는 3*3 배열 추출
    def getTempArray(position):
        temp = []
        cx, cy = position
        for i in range(-1,2):
            temp.append(temp_matrix[cy+i][cx-1:cx+2])
            for j in range(-1, 2):
                explore_list.add((cx + j, cy + i))
        return temp
    
    temp_arr = getTempArray(position)

    # 90도 회전
    if rotating_degree == 90:
        # 2차원 배열을 뒤집어 전치하면 90도 회전
        temp_arr = list(zip(*temp_arr[::-1]))

    # 180도 회전
    elif rotating_degree == 180:
        # 2차원 배열을 뒤집어 전치하면 90도 회전
        # 해당 회전 2회
        for _ in range(2):
            temp_arr = list(zip(*temp_arr[::-1]))

    # 270도 회전
    elif rotating_degree == 270:
        # 2차원 배열을 뒤집어 전치하면 90도 회전
        # 해당 회전 3회
        for _ in range(3):
            temp_arr = list(zip(*temp_arr[::-1]))

    # 돌린 3*3 배열을 삽입
    for i in range(-1, 2):
        for j in range(-1, 2):
            temp_matrix[position[1]+i][position[0]+j] = temp_arr[i+1][j+1]
    
    # 삽입완료한 5*5배열, bfs 돌릴 시작 좌표 리스트, 중심좌표, 회전 각도를 인자로 bfs함수 실행
    rotate_result = canGet(temp_matrix, explore_list, position, rotating_degree)

    return rotate_result, temp_matrix


K, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(5)]

relics = deque(list(map(int, input().split())))

total_relics = 0

result = []

# 1. 탐사 진행 result의 요소 개수가 탐사 횟수
while len(result) < K:
    # 최종 좌표 및 회전 각
    max_relics_count = -1
    min_rotating_degree = float('inf')
    max_rotating_position = (-1, -1)
    max_relics_visited = []
    max_relics_matrix = []

    # 우선순위 고려해서 최종 회전시킬 좌표 및 회전 각 찾기
    for y in range(1, 4):
        for x in range(1, 4):
            for degree in range(90, 271, 90):
                (temp_relics, rotating_position, rotating_degree, temp_visited), temp_matrix = rotate((x, y), degree)

                # 획득 유물 가장 많은 경우
                if temp_relics > max_relics_count:
                    max_relics_count = temp_relics
                    min_rotating_degree = rotating_degree
                    max_rotating_position = rotating_position
                    max_relics_visited = temp_visited
                    max_relics_matrix = temp_matrix

                # 회전한 각도가 가장 작은 경우
                elif temp_relics == max_relics_count and rotating_degree < min_rotating_degree:
                    max_relics_count = temp_relics
                    min_rotating_degree = rotating_degree
                    max_rotating_position = rotating_position
                    max_relics_visited = temp_visited
                    max_relics_matrix = temp_matrix

                # 열이 작거나 같은 경우
                elif temp_relics == max_relics_count and rotating_degree == min_rotating_degree and rotating_position[0] <= max_rotating_position[0]:
                    
                    # 열이 작은 경우
                    if rotating_position[0] < max_rotating_position[0]:
                        max_relics_count = temp_relics
                        min_rotating_degree = rotating_degree
                        max_rotating_position = rotating_position
                        max_relics_visited = temp_visited
                        max_relics_matrix = temp_matrix
                    
                    # 행이 작은 경우
                    elif rotating_position[1] < max_rotating_position[1]:
                        max_relics_count = temp_relics
                        min_rotating_degree = rotating_degree
                        max_rotating_position = rotating_position
                        max_relics_visited = temp_visited
                        max_relics_matrix = temp_matrix

    # 탐사 후 발견된 유물이 0개인 경우 탐사 종료
    if max_relics_count == 0:
        break
    
    total_relics += max_relics_count

    # 유물 채우기
    for i in range(5):
        for j in range(4, -1, -1):
            if max_relics_visited[j][i]:
                max_relics_matrix[j][i] = relics.popleft()

    matrix = [a[:] for a in max_relics_matrix]

    
    while True:
        # 연쇄 유물 획득
        temp_relics, rotating_position, rotating_degree, temp_visited = canGet(matrix, {(i, j) for i in range(5) for j in range(5)}, (-1, -1), 0, after_rotating=False)
        # 유물을 획득한 경우
        if temp_relics:
            total_relics += temp_relics
            # 유물 채우기
            for i in range(5):
                for j in range(4, -1, -1):
                    if temp_visited[j][i]:
                        matrix[j][i] = relics.popleft()
            
        # 유물을 획득하지 못한 경우
        else:
            result.append(str(total_relics))
            total_relics = 0
            break

print(" ".join(result))