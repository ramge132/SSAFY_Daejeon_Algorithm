# DP 방식
# dp[x][y][d] : (x,y)위치에 d 방향으로 도달하는 경우의 수
# 방향: 0(가로), 1(대각선), 2(세로)
# dp의 3차원 리스트: 1차원 = x, 2 차원 = y, 3차원 = 방향
# EX) x = 5 일 때,
# [[0,0,0], [0,0,0], [0,0,0], [0,0,1], [0,1,4], [1,4,8]]
# 마지막 [1,4,8]은 해당 x,y 좌표에 해당하는 [가로, 대각선, 세로] 의 개수가 저장되있다.

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

if lst[N-1][N-1] == 1:  # 도착점이 벽이면 바로 종료
    print(0)
else:
    dp = [[[0]*3 for _ in range(N)] for _ in range(N)] # 3차원 배열 생성. x y dir
    
    # 초기 상태 설정
    dp[0][1][0] = 1

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1: # 1이면 해당 좌표 무시
                continue

            if j+1 < N and lst[i][j+1] == 0: # 가로 방향으로 이동
                dp[i][j+1][0] += dp[i][j][0] + dp[i][j][1]

            if i+1 < N and lst[i+1][j] == 0: # 세로 방향으로 이동
                dp[i+1][j][2] += dp[i][j][1] + dp[i][j][2]

            if i+1 < N and j+1 < N and lst[i+1][j] == 0 and lst[i][j+1] == 0 and lst[i+1][j+1] == 0: # 대각선 방향으로 이동
                dp[i+1][j+1][1] += dp[i][j][0] + dp[i][j][1] + dp[i][j][2]

    # print(dp)
    print(sum(dp[N-1][N-1]))



## 기본적인 BFS 방식 풀이
## BFS로 풀면 시간 초과가 난다.

# from collections import deque

# DXY = [(0, 1), (1, 1), (1, 0)]

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]
# queue = deque([])
# total = 0

# queue.append([0, 1, 0]) # 초기 위치 설정, 방향은 0 (오른쪽)

# def chk_dir(dir, dxy):
#     if dir == 0 and dxy == 2: # 가로 세로에 안되는 경우는 하나씩 만 존재.
#         return False
#     if dir == 2 and dxy == 0:
#         return False
#     else: # 나머지 전부 가능
#         return True

# while queue:
#     x, y, c_dir = queue.popleft() # queue에 저장된 좌표를 빼서 사용

#     if x == N - 1 and y == N - 1:
#         total += 1

#     for idx in range(len(DXY)): # 각 방향을 확인
#         nx, ny = x + DXY[idx][0], y + DXY[idx][1]

#         if nx < 0 or nx >= N or ny < 0 or ny >= N: # 다음 위치로 갈 수 없을 때,
#             continue
#         if not chk_dir(c_dir, idx): # 방향 chk 통과하지 못하면 무시
#             continue
#         if idx == 1 and lst[nx][ny] == 1 or lst[x][ny] == 1 or lst[nx][y] == 1: 
#              continue
#         if idx != 1 and lst[nx][ny] == 1:
#             continue

#         queue.append([nx, ny, idx]) # 다음 위치로 갈 수 있으면 저장
# print(total)


## for 문을 이용하지 않은 방법

# DXY 리스트를 이용해서 방향을 할당하여 for문을 이용하는 것이 아닌
# 직접 인덱스 값을 할당
# for문으로 값을 순회하지 않고 하나의 방향 값에 대해서 if문을 전부 거치게 하여 가능한 방향 값들을 append 하도록 만듦 << 진짜 천재임?

# from collections import deque

# def solution(N, board):
#     # 방향: 0(가로), 1(대각선), 2(세로)
#     queue = deque([(0, 1, 0)])
#     count = 0

#     while queue:
#         x, y, d = queue.popleft()
        
#         if x == N-1 and y == N-1:
#             count += 1
#             continue

#         # 가로 이동
#         if d in [0, 1] and y + 1 < N and board[x][y+1] == 0:
#             queue.append((x, y+1, 0))
        
#         # 세로 이동
#         if d in [1, 2] and x + 1 < N and board[x+1][y] == 0:
#             queue.append((x+1, y, 2))
        
#         # 대각선 이동
#         if x + 1 < N and y + 1 < N and board[x+1][y] == 0 and board[x][y+1] == 0 and board[x+1][y+1] == 0:
#             queue.append((x+1, y+1, 1))

#     return count

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]

# print(solution(N, board))

