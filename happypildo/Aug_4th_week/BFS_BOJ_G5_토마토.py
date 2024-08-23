"""
# 문제 설명:
- 격자판에 익은 토마토와 익지 않은 토마토, 빈 칸이 존재한다.
- 익은 토마토는 영향력을 상하좌우로 퍼트려, 익지 않은 토마토가 있을 때 익게 만든다.
- 이러한 상황에서, 모든 토마토가 익기 위해서 최소 얼마나 걸리는가? (모든 토마토가 익을 수 없다면 -1을 출력한다.)

# 접근 방법:
- 전형적인 BFS 문제로, BFS 활용법에 약한 것 같아 풀어보고 있습니다.
- BFS를 돌릴 때 depth를 어떻게 조절할지 / 초반에 여러 익은 토마토가 있을 경우 어떻게 처리할지를 중점으로 고민했습니다.
"""
from collections import deque
from pprint import pprint

DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def BFS(N, M, tomato):
    depth = 0
    queue = deque()
    is_visited = {}
    set_of_all = set()

    for x in range(N):
        for y in range(M):
            if tomato[x][y] == 1:
                queue.append((x, y, 0))
                is_visited[(x, y)] = 0
            if tomato[x][y] != -1:
                set_of_all.add((x, y))

    while queue:
        item = queue.popleft()
        x, y, depth = item

        for direction in DIRECTION:
            dx, dy = direction
            temp_x, temp_y = x + dx, y + dy

            if (-1 < temp_x < N) and (-1 < temp_y < M):
                if tomato[temp_x][temp_y] == 0 or tomato[temp_x][temp_y] == 1:
                    if is_visited.get((temp_x, temp_y), None) is None:
                        is_visited[(temp_x, temp_y)] = depth + 1
                        queue.append((temp_x, temp_y, depth + 1))
                    else:
                        if is_visited[(temp_x, temp_y)] > depth + 1:
                            queue.append((temp_x, temp_y, depth + 1))

    if set_of_all == set(list(is_visited.keys())):
        return max(list(is_visited.values()))
    else:
        return -1

M, N = list(map(int, input().split()))

tomato = [list(map(int, input().split())) for n in range(N)]

print(BFS(N, M, tomato))
