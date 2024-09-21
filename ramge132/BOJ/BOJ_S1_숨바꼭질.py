# https://www.acmicpc.net/problem/1697

from collections import deque

MAX_POSITION = 100000  # 수빈이가 이동할 수 있는 최대 위치


def bfs(N, K):
    visited = [-1] * (MAX_POSITION + 1)  # 0부터 100,000까지
    visited[N] = 0  # 수빈이가 있는 위치를 0초로 시작

    # BFS를 위한 큐 초기화
    queue = deque([N])

    while queue:
        current = queue.popleft()

        # 현재 위치가 동생의 위치라면 그때의 시간이 최단 시간
        if current == K:
            return visited[current]

        # 3가지 이동 방법에 대해 각각 탐색
        for next_pos in (current - 1, current + 1, current * 2):
            if 0 <= next_pos <= 100000 and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)


N, K = map(int, input().split())
result = bfs(N, K)
print(result)
