# # 시작 13:40

# # 상하좌우
# dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# def dfs(pos, can_crash, distance):
#     global min_distance
#     # 현재 좌표가 (m, n)인 경우 종료
#     if pos == (M, N):
#         min_distance = distance
#         return
    
#     # 가지치기
#     # 현재 최단거리보다 길어지는 경우
#     if distance >= min_distance:
#         min_distance  = -1
#         return

#     cx, cy = pos
#     # 4방향 탐색
#     for dx, dy in dxy:
#         nx, ny = cx + dx, cy + dy

#         # 영역 밖인 경우
#         if not (0 <= nx <= M-1 and 0 <= ny <= N-1):
#             continue

#         # 벽인경우
#         if matrix[ny][nx] == 1:
#             # 부술 수 있는 경우
#             if can_crash:
#                 dfs((nx, ny), False, distance+1)
#             # 못 부수는 경우
#             else:
#                 continue

#         # 이동 가능한 경우
#         dfs((nx, ny), can_crash, distance+1)
    

# N, M = map(int, input().split())
# matrix = [list(map(int, list(input()))) for _ in range(N)]
# min_distance = float('inf')

# dfs((0, 0), True, 1)

############################################################################################

from collections import deque

# 상하좌우
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def bfs(queue):
    while queue:
        cx, cy, crash_time, distance = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            
            # 영역 밖인 경우
            if not (0 <= nx <= M-1 and 0 <= ny <= N-1):
                continue

            # 목적지인 경우
            if (nx, ny) == (M-1, N-1):
                return distance + 1
            
            # 방문 확인
            if matrix[ny][nx][1]:
                # 벽인 경우 깰수 있는지
                if matrix[ny][nx][0] == 1 and crash_time == 0:
                    queue.append((nx, ny, 1, distance + 1))
                    matrix[ny][nx][1] = False

                # 이동할 수 있는 곳
                elif matrix[ny][nx][0] == 0:
                    queue.append((nx, ny, crash_time, distance + 1))
                    matrix[ny][nx][1] = False
    
    return -1

N, M = map(int, input().split())
matrix = [list(map(lambda x: [int(x), True], list(input()))) for _ in range(N)]

# x, y, 벽을 깬 여부, 거리
queue = deque([(0, 0, 0, 1)])

print(bfs(queue))

############################################################################################

from collections import deque

# 우하좌상
dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def bfs(queue):
    while queue:
        cx, cy, crash_time, distance = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            
            # 영역 밖인 경우
            if not (0 <= nx <= M-1 and 0 <= ny <= N-1):
                continue

            # 목적지인 경우
            if (nx, ny) == (M-1, N-1):
                return distance + 1
            
            # 방문 확인
            if visited[ny][nx]:
                # 벽인 경우 깰수 있는지
                if matrix[ny][nx] == 1 and crash_time == 0:
                    queue.append((nx, ny, 1, distance + 1))
                    visited[ny][nx] = False

                # 이동할 수 있는 곳
                elif matrix[ny][nx] == 0:
                    queue.append((nx, ny, crash_time, distance + 1))
                    visited[ny][nx] = False
    
    return -1

N, M = map(int, input().split())
matrix = [list(map(int, list(input()))) for _ in range(N)]
visited = [[True] * M for _ in range(N)]

# x, y, 벽을 깬 여부, 거리
queue = deque([(0, 0, 0, 1)])

print(bfs(queue))







