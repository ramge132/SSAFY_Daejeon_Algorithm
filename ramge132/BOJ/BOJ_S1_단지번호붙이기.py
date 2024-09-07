# https://www.acmicpc.net/problem/2667

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS로 연결된 집들을 탐색하는 함수
def dfs(x, y, N, grid, visited):
    stack = [(x, y)]
    visited[x][y] = True
    house_count = 1
    
    while stack:
        cx, cy = stack.pop()
        # 상하좌우 방향으로 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
                house_count += 1
    return house_count

def find_complexes(N, grid):
    visited = [[False] * N for _ in range(N)]
    complexes = []

    # 모든 좌표를 순회하며 DFS 탐색을 수행
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1 and not visited[i][j]:
                # 새로운 단지를 발견하면 DFS를 통해 단지 크기를 계산
                complex_size = dfs(i, j, N, grid, visited)
                complexes.append(complex_size)

    return sorted(complexes)

N = int(input())
grid = [list(map(int, input().strip())) for _ in range(N)]

complexes = find_complexes(N, grid)

print(len(complexes))
for size in complexes:
    print(size)
