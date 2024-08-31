"""
# 문제 설명
- N by M 미로가 있다. 1은 벽이고 0은 길이다.
- (1, 1)에서 (N, M)으로 이동하는 최소 거리를 알고 싶은데, 만약 벽을 부수고 가는 것이 더 짧다면 딱 한 번 부술 수 있다.

# 접근법
- 처음엔 DFS로 경우의 수를 모두 탐방하고자 했으나 (벽을 만나면 일단 부숨), recurssion error가 발생했습니다.
- 그래서 BFS로 진행을 하고자 했고, 다음과 같이 접근했습니다.
    1. 일단, 벽을 부수지 않는 경로에 대한 최소 거리를 계산한다. (못 갈 수도 있다.)
    2. 해당 최소 거리를 기반으로, 각 벽에 대한 거리를 계산한다. (즉, 한 번 부술 때 그 거리)
    3. 이후, 부순 적이 있다면, (2)의 결과를 토대로 BFS를 진행한다.
        - 이 때 벽을 다시 부수면 안되기 때문에 '0'인 길로만 간다.
"""
from collections import deque

DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def BFS(N, M, maze):
    queue = deque()
    queue.append((0, 0)) 

    queue_for_integ = deque()

    
    price_map = [[float('inf') for m in range(M)] for n in range(N)]                # 벽을 부수지 않고 간 배열
    price_map_with_broken = [[float('inf') for m in range(M)] for n in range(N)]    # 벽을 단 한 번 부수고 간 배열
    has_broken = False          # 벽을 한 번이라도 부쉈는지?
    price_map[0][0] = 0

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTION:
            temp_x, temp_y = x + dx, y + dy
            
            if (-1 < temp_x < N) and (-1 < temp_y < M):
                if maze[temp_x][temp_y] == '0':
                    prev_price = price_map[temp_x][temp_y]
                    incoming_price = price_map[x][y] + 1

                    if prev_price > incoming_price:         # 벽을 부수지 않고 간 배열에 대한 BFS
                        price_map[temp_x][temp_y] = incoming_price
                        queue.append((temp_x, temp_y))
                else:
                    prev_price = price_map_with_broken[temp_x][temp_y]
                    incoming_price = price_map[x][y] + 1

                    if prev_price > incoming_price:     # 벽을 연속으로 부술 수 없기 떄문에, queue.append를 하지 않음
                        price_map_with_broken[temp_x][temp_y] = incoming_price
                        queue_for_integ.append((temp_x, temp_y))    # 이후, 벽을 부순 것과 부수지 않은 것을 통합하기 위해 queue_for_integ 큐에 삽입
                        has_broken = True
    if has_broken:
        while queue_for_integ:
            x, y = queue_for_integ.popleft()
            
            for dx, dy in DIRECTION:
                temp_x, temp_y = x + dx, y + dy

                if (-1 < temp_x < N) and (-1 < temp_y < M):
                    if maze[temp_x][temp_y] == '0':
                        # 부순 적이 있기 때문에, 0으로만 간다.
                        prev_price = price_map_with_broken[temp_x][temp_y]
                        incoming_price = price_map_with_broken[x][y] + 1
                        if prev_price > incoming_price:
                            price_map_with_broken[temp_x][temp_y] = incoming_price
                            queue_for_integ.append((temp_x, temp_y))
        return price_map_with_broken[N - 1][M - 1] + 1
    else:
        return price_map[N - 1][M - 1] + 1

N, M = list(map(int, input().split()))

maze = [input() for n_iter in range(N)]
answer = BFS(N, M, maze)
answer = -1 if answer == float('inf') else answer
print(answer)