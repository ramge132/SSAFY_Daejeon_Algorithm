dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def dfs(pos, crashed_wall):
    cx, cy = pos
    for dx, dy in dxy:
        nx, ny = cx + dx, cy + dy
        # 범위 밖으로 나간 경우
        if not (0 <= nx <= N-1 and 0 <= ny <= M-1):
            continue

        # 벽 만난 경우
        if maze[ny][nx] == 1:
            pass

        # 그냥 이동 가능
        '''
        
        수정 중
        
        '''
    pass

N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(M)]

min_wall = float('inf')

dfs((0, 0))

print(min_wall)