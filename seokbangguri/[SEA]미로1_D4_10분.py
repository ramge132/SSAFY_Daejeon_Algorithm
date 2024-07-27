dxy = [[-1,0],[1,0],[0,-1],[0,1]]
# DFS 깊이 우선 탐색 버전 시간 복잡도 O(2^(가로*세로)) >> 미로 찾기에 시간복잡도 좋지 않음
# 하지만 특정 경로를 지나쳐 가야하면 깊이 우선 탐색 이용해야 함
'''
def find_route_dfs(x, y):
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if maze[ny][nx] == 0:
            maze[ny][nx] = 1
            if find_route_dfs(nx, ny) == 1:
                return 1
        elif maze[ny][nx] == 3:
            return 1
    return 0

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{t} {find_route_dfs(1,1)}')
    # ///////////////////////////////////////////////////////////////////////////////////
'''
# BFS 너비 우선 탐색 버전
from collections import deque
def find_route_bfs():
    while len(Q):
        x, y = Q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 미로의 레인지를 넘어가는 경우 진행 X
            n = len(maze)
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue

            if maze[ny][nx] == 0:
                maze[ny][nx] = 1
                Q.append((nx, ny))

            elif maze[ny][nx] == 3:
                return 1
    return 0

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    Q = deque([(1,1)])

    print(f'#{t} {find_route_bfs()}')