import sys
sys.stdin = open('등산로조성.txt', 'r')

from collections import deque

# T = int(input())
# DXY = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def is_valid(nx, ny):
#     return 0 <= nx < N and 0 <= ny < N

# def dfs(x, y, length, cnt, current_h):
#     global max_length
#     max_length = max(max_length, length)
    
#     for dx, dy in DXY:
#         nx, ny = x + dx, y + dy
#         if not is_valid(nx, ny): continue
        
#         if lst[nx][ny] < current_h:
#             dfs(nx, ny, length + 1, cnt, lst[nx][ny])

#         elif cnt > 0 and lst[nx][ny] - cnt < current_h:
#             new_height = current_h - 1
#             dfs(nx, ny, length + 1, 0, new_height)

# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#     lst = [list(map(int, input().split())) for _ in range(N)]

#     max_h = 0
#     max_length = 0
#     for i in range(N):
#         for j in range(N):
#             max_h = max(max_h, lst[i][j])

#     # 방향 지정
#     # x, y를 가져온 후, 방향을 지정해서 queue에 저장
#     # 방문한 좌표는 방문 x

#     for i in range(N):
#         for j in range(N):
#             if lst[i][j] == max_h:
#                 dfs(i, j, 1, K, lst[i][j]) # 초기 위치, 공사 가능 높이 K, 현재 값

#     print(f'#{test_case} {max_length}')

# BFS 풀이
# visited를 사용하지 못함
# 4번 이외의 다른 것들 또한 전부 확인하지 못한다.

T = int(input())
DXY = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_valid(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    max_h = 0
    max_length = 0
    for i in range(N):
        for j in range(N):
            max_h = max(max_h, lst[i][j])

    # 방향 지정
    # x, y를 가져온 후, 방향을 지정해서 queue에 저장
    # 방문한 좌표는 방문 x


    for i in range(N):
        for j in range(N):
            
            if lst[i][j] == max_h:
                queue = deque([(i, j, 1 , K, lst[i][j])]) # 좌표, 길이, 공사 가능 높이, 현재 값     
                # visited = {v:[] for v in range(N)} # 방문 좌표 저장 딕셔너리

                while queue:
                    x, y, current_length, cnt, current_h = queue.popleft()

                    for dx, dy in DXY:
                        nx, ny = x + dx, y + dy
                        if not is_valid(nx, ny): continue

                        # if (nx, ny) in visited: continue # 방문했을 때, 탐색하지 않도록 만든다.
                        # visited[nx].append(ny) # 방문을 하지 않았을 때, 
                        
                        if lst[nx][ny] >= current_h: # 값이 크거나 같을 때
                            # 만약 현재 높이를 K로 뺐을 때, 다음 지점보다 작은지 확인
                            if lst[nx][ny] - cnt < current_h: # 공사가 가능할 때,
                                # k = lst[nx][ny] - (current_h - 1)
                                # lst[nx][ny] = lst[x][y] - 1
                                # cnt -= k
                                queue.append((nx, ny, current_length + 1, 0, current_h - 1))
                                continue
                            
                            else: # 등산로 조성 완료    
                                max_length = max(max_length, current_length)
                                continue
                        
                        else: # 다음 위치가 더 작을 때, 저장    
                            queue.append((nx, ny, current_length + 1, cnt, lst[nx][ny]))
                            continue
                
                # lst = tmp_lst[:] # while문이 끝난 후, 원상 복구

    print(f'#{test_case} {max_length}')