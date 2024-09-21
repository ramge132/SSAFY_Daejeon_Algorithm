import sys

sys.stdin = open('input.txt')

from collections import deque

M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(box)

# 6방향을 나타내는 벡터 (위, 아래, 왼쪽, 오른쪽, 앞, 뒤)
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 익은 토마토의 좌표를 저장할 큐
queue = deque()

# 처음 상태에서 익은 토마토를 큐에 모두 넣기
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 1:
                queue.append((x, y, z))
while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and tomatoes[nz][ny][nx] == 0:
            tomatoes[nz][ny][nx] = tomatoes[z][y][x] + 1
            queue.append((nx, ny, nz))

days = 0
for z in range(H):
    for y in range(N):
        for x in range(M):
            if tomatoes[z][y][x] == 0:  # 익지 않은 토마토가 남아있으면
                print(-1)
                exit(0)
            days = max(days, tomatoes[z][y][x])

# 처음부터 모두 익은 상태면 0, 그렇지 않으면 걸린 날짜에서 1을 뺀 값 출력
print(days - 1 if days > 1 else 0)
