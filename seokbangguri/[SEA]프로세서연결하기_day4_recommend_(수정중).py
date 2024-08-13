import sys
from pprint import pprint
sys.stdin = open('core.txt')

# 상 하 좌 우 연결 안함
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0], [0, 0]]

def dfs(cur_position, total_line_count, cells, connected_core, visited):
    global result
    temp_visited = visited
    temp_cells = cells
    cx, cy = cur_position

    # 이미 작업한 프로세서 인 경우 다음 프로세서 찾기
    # pprint(temp_visited)
    if temp_visited[cy][cx] == True:
        test_visited_core.add((cx, cy))
        found_next_core = False
        while not found_next_core:
            for _ in range(1, N-cx):
                # print('cx', cx+1, 'cy', cy)
                if cells[cy][cx + 1] == 1:
                    # print('core', cx, cy)
                    found_next_core = True
                    cx += 1
                    break
                cx += 1
            # 끝까지 다 탐색했으면 리턴
            if cx == N-1 and cy == N-1:
                if result:
                    if result[0] <= connected_core and result[1] <= total_line_count:
                        result = [connected_core, total_line_count]
                return

            if not found_next_core:
                cx = 0
                if cy != N-1:
                    cy += 1
    # print('cur_pos', cx, cy)

    # 모서리 코어 일 경우
    if cx == 0 or cy == 0 or cx == N-1 or cy == N-1:
        temp_visited[cy][cx] = True
        dfs((cx, cy), total_line_count, temp_cells, connected_core + 1, temp_visited)

    else:
        for x, y in dxy:
            nx, ny = cx + x, cy + y
            temp_line_count = 0
            # 전원 연결 성공 여부
            is_success = True
            while nx > 0 and nx < N-1 and ny > 0 and ny < N-1 and (x or y):
                nx, ny = nx + x, ny + y

                # 모서리에 도달하기 전 다른 프로세스 또는 전선 만날 경우 
                if temp_cells[ny][nx] == 1:
                    is_success = False
                    break

                temp_line_count += 1

            if is_success:
                # print((cx, cy), total_line_count + temp_line_count, temp_cells, connected_core + 1, temp_visited)
                temp_visited[cy][cx] = True
                if x or y:
                    dfs((cx, cy), total_line_count + temp_line_count, temp_cells, connected_core + 1, temp_visited)
                else:
                    dfs((cx, cy), total_line_count + temp_line_count, temp_cells, connected_core, temp_visited)




T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = [0, 0]
    start_point = (0, 0)

    test_visited_core = set()

    found_first = False
    for y in range(N):
        for x in range(N):
            if cells[y][x]:
                start_point = (x, y)
                found_first = True
                break
        if found_first:
            break

    dfs(start_point, 0, cells, 0, visited)
    print(result)
    print(list(test_visited_core))




    # break