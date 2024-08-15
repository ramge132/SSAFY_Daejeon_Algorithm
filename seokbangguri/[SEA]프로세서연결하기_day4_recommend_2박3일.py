import sys
# from pprint import pprint
sys.stdin = open('input.txt')

# 상 하 좌 우
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def dfs(cells, cores_pos, connected_cores, elec_line, depth):
    global result
    # 현재 연결된 코어보다 최대 코어 수가 적으면 더 탐색할 필요가 없음
    if connected_cores + (len(cores_pos) - depth) < result[0]:
        return
    
    if depth >= len(cores_pos):
        if connected_cores > result[0]:
            result = [connected_cores, elec_line]
            # pprint(cells)
        elif connected_cores == result[0] and elec_line < result[1]:
            result = [connected_cores, elec_line]
            # pprint(cells)
        return
    
    # 코어의 위치
    cx, cy = cores_pos[depth]

    # 모서리 코어인 경우
    if cx == 0 or cy == 0 or cx == N - 1 or cy == N - 1:
        dfs(cells, cores_pos, connected_cores+1, elec_line, depth+1)

    # 모서리 코어가 아닌 경우
    else:
        # 방향 지정
        for x, y in dxy:
            temp_cells = [a[:] for a in cells]
            nx, ny = cx + x, cy + y
            is_available = True
            temp_lines = 0

            # 지정한 방향으로 전선을 연결 할 수 있는지 확인
            while nx >= 0 and ny >= 0 and nx <= N-1 and ny <= N-1:
                if temp_cells[ny][nx] != 0:
                    is_available = False
                    break

                nx += x
                ny += y

            # 연결 가능한 경우 선 그어주기
            if is_available:
                nx, ny = cx + x, cy + y
                while 0 <= nx <= N-1 and 0 <= ny <= N-1:
                    # 전선 2로 표시
                    temp_cells[ny][nx] = 2
                    temp_lines += 1
                    nx += x
                    ny += y
                
                dfs(temp_cells, cores_pos, connected_cores+1, elec_line + temp_lines, depth+1)
            
            # 연결하지 않고 넘어가는 경우
            dfs(cells, cores_pos, connected_cores, elec_line, depth + 1)
                    

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cells = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    result = [0, float('inf')]
    core_points = []

    # 시작점 찾기
    found_first = False
    for y in range(N):
        for x in range(N):
            if cells[y][x]:
                core_points.append((x, y))

    dfs(cells, core_points, 0, 0, 0)
    print(f'#{test_case} {result[1]}')
    # break
