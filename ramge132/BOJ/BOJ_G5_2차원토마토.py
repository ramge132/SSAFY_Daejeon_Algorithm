import sys
sys.stdin = open('input.txt')

from collections import deque


def bfs(M, N, tomatoes):
    # 네 방향 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 익은 토마토의 좌표를 저장할 큐
    queue = deque()

    # 처음 상태에서 익은 토마토를 큐에 모두 넣기
    for y in range(N):
        for x in range(M):
            if tomatoes[y][x] == 1:
                queue.append((x, y))

    # BFS 수행
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and tomatoes[ny][nx] == 0:
                tomatoes[ny][nx] = tomatoes[y][x] + 1
                queue.append((nx, ny))

    # 최소 일수를 계산하고, 익지 않은 토마토가 남아있는지 확인
    days = 0
    for y in range(N):
        for x in range(M):
            if tomatoes[y][x] == 0:  # 익지 않은 토마토가 있으면 -1 반환
                return -1
            days = max(days, tomatoes[y][x])

    # 처음부터 모두 익은 상태면 0, 그렇지 않으면 걸린 날짜에서 1을 뺀 값 반환
    return days - 1 if days > 1 else 0


M, N = map(int, input().split())  # M: 가로, N: 세로
tomatoes = [list(map(int, input().split())) for _ in range(N)]

result = bfs(M, N, tomatoes)
print(result)

