from collections import deque

def bfs(maze, n, m):
    # 이동 방향: 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0)])  # 시작점 (0, 0)에서 출발
    maze[0][0] = 1  # 시작점의 거리

    while queue:
        x, y = queue.popleft()
        
        # 도착 지점에 도달하면 현재까지의 이동 칸 수를 반환
        if x == n - 1 and y == m - 1:
            return maze[x][y]
        
        # 인접한 칸 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # 미로 내부이고 이동 가능한 칸이라면
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                # 다음 칸으로 이동하고, 이동 칸 수를 기록
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(n)]

result = bfs(maze, n, m)

print(result)