import sys, pprint
sys.stdin = open('프로세서_연결하기.txt', 'r')

T = int(input())

# main
# 프로세서 연결을 위해 DXY에 설정된 방향으로 dfs를 돌면서 연결 한다.

# dfs
# 연결이 가능할 때를 확인하도록 chk_next 함수를 정의해서 탐색 여부를 확인한다.
# 만약 연결이 가능하면 set_core 함수를 사용하여 리스트에 2를 작성하여 전선을 표시한다.
# 총 연결된 코어의 개수가 max보다 크거나 같고, 길이가 작으면 저장을 한다.

# 현재 코어의 개수와 이후에 얻을 수 있는 코어의 총 개수가 max_core보다 작을 때, 답이 될 수 없기 때문에 종료한다.
# 현재 코어를 선택하지 않을 경우를 생각한다. 

# 원래 아이디어에선 연결 가능을 먼저 파악하지 않고 리스트에 2를 연결해 가면서 만약에 다음 값이 1, 2가 나왔을 때, 
# 연결하지 못하므로 다시 2로 작성된 값들을 0으로 설정하면서 복구를 하는 방식을 생각하였다.
# 연결 여부를 파악하지 않고 2를 먼저 작성해 나간 다음 만약 다음값이 연결하지 못하는 값이면 다시 0으로 설정하는 불필요한 연산을 하였다.
# 이를 chk_next를 이용해서 끝까지 먼저 탐색을 한 후, 연결 여부를 확인하는 방식으로 변경을 하였다.

DXY = [(1,0), (-1,0), (0,-1), (0, 1)] # 0 1 2 3

def chk_next(x, y, direction):                             # 선택한 코어의 방향에 따라 연결 여부를 확인한다. 0으로 탐색이 마무리 되면 True, 0이 아닌값이 나오면 False
    dx, dy = DXY[direction]
    nx, ny = x + dx, y + dy

    while 0 <= nx < N and 0 <= ny < N:
        if lst[nx][ny] != 0:
            return False
        nx += dx
        ny += dy
    return True

def set_core(x, y, direction, value):                      # 코어를 연결할 수 있으면, 해당 위치 까지 2로 리스트에 작성을 한다.
    dx, dy = DXY[direction]
    nx, ny = x + dx, y + dy
    length = 0

    while 0 <= nx < N and 0 <= ny < N:
        lst[nx][ny] = value
        nx += dx
        ny += dy
        length += 1

    return length

def dfs(idx, total, connected):
    global min_len, max_connected

    if idx == len(cores):
        if connected > max_connected or (connected == max_connected and total < min_len): # 만약 코어 연결 수가 크거나 같고, 기존 전선의 길이 보다 작을 때
            max_connected = connected
            min_len = total
        return

    if connected + len(cores) - idx < max_connected:        # 만약 연결된 코어의 개수 + 탐색 가능한 코어 수(모든 코어의 개수 - 현재 확인하는 코어 수)가 max_connect보다 작으면 종료한다.
        return
    
    x, y = cores[idx]
    
    if x == 0 or x == N - 1 or y == 0 or y == N - 1:        # 만약 외곽에 존재하여 전선 연결이 필요 없는 코어인 경우 dfs로 이동
        dfs(idx + 1, total, connected + 1)
        return

    dfs(idx + 1, total, connected)                          # 현재 코어를 선택하지 않을 경우

    for direction in range(len(DXY)):                       # 방향 선택
        if chk_next(x, y, direction):                       # chk_next를 통해 선택된 방향에 전선 혹은 코어가 존재하지 않을 경우 True
            length = set_core(x, y, direction, 2)           # 리스트에 전선을 연결한 길이를 반환
            dfs(idx + 1, total + length, connected + 1)     # cores 리스트의 다음 index로 이동, 총 길이 + 현재 길이, 연결 + 1 
            set_core(x, y, direction, 0)                    # 재귀가 끝난 후 복귀하였을 때, 리스트를 원래대로 복구를 해야 다음 dfs에서 원상복구된 리스트를 사용할 수 있다.

for test_case in range(1, T+1):
    N = int(input())
    lst = [list(map(int,input().split())) for _ in range(N)]
    cores = []
    min_len = float('inf')
    max_connected = 0

    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                cores.append((i,j))                         # 코어의 좌표를 cores 리스트에 저장한다. > 코어의 값은 변경되면 안되기 떄문에 tuple을 사용

    dfs(0, 0, 0)

    print(f'#{test_case} {min_len}')


# T = int(input())

# DXY = [(1, 0), (-1, 0), (0, -1), (0, 1)]

# # pro_lst에 코어들의 좌표를 저장한다.

# def dfs(idx, cores, length): # 결과적으로 필요한 값 => 코어 개수 / 길이, 종료 조건
#     global pro_lst, min_len
    
#     current_length = 0

#     pprint.pprint(lst)
#     print(cores, length)

#     if length > min_len: # 가지치기
#         return

#     if idx == len(pro_lst): # 종료 조건
#         if max_cores <= cores and min_len > length:
#             min_len = length
#         return
    
#     x, y = pro_lst[idx][0], pro_lst[idx][1]
    
#     if lst[x][y] == 1 and x == 0 or x == N - 1 or y == 0 or y == N - 1:
#         dfs(idx + 1, cores + 1, length)
#         return

#     for dx, dy in DXY:
#         nx, ny = x + dx, y + dy # 다음 위치

#         if not (0 <= nx <= N - 1 and 0 <= ny <= N - 1): continue

#         print(f'chk {nx} {ny}')
#         while not (0 <= nx <= N - 1 and 0 <= ny <= N - 1):
#             if lst[nx][ny] == 1 or 2:
#                 nx -= dx
#                 ny -= dy
#                 while nx != x or ny != y:
#                     lst[nx][ny] = 0
#                 break
                
#             print(f'chk x y')
#             lst[nx][ny] = 2
#             nx += dx
#             ny += dy
#             current_length += 1
        
#         dfs(idx + 1, cores + 1, length + current_length)

#         nx -= dx
#         ny -= dy
#         while nx != x or ny != y:
#             print(x, y, nx, ny)
#             lst[nx][ny] = 0
#             nx -= dx
#             ny -= dy
    



# for test_case in range(1, T + 1):
#     N = int(input())
#     lst = [list(map(int, input().split())) for _ in range(N)]
    
#     max_cores = 0
#     min_len = float('inf')
    
#     pro_lst = []

#     for i in range(N):
#         for j in range(N):
#             if lst[i][j] == 1:
#                 pro_lst.append([i,j])
    
#     dfs(0, 0, 0)
#     print(f'#{test_case} {min_len}')
#     break


# import sys
# sys.stdin = open('프로세서_연결하기.txt', 'r')

# T = int(input())

# DXY = [(1,0), (-1,0), (0,-1), (0, 1)] # 0 1 2 3

# def chk_len(chk_lst):
#     if chk_lst[2] == 0:
#         return (N - 1) - chk_lst[0]
#     elif chk_lst[2] == 1:
#         return chk_lst[0]
#     elif chk_lst[2] == 2:
#         return chk_lst[1]
#     elif chk_lst[2] == 3:
#         return (N - 1) - chk_lst[1]

# def chk(chk_lst, pro_lst):
#     x, y, direction = chk_lst
#     dx, dy = DXY[direction]
#     nx, ny = x, y

#     while 0 <= nx < N and 0 <= ny < N:
#         nx += dx
#         ny += dy
#         for px, py, _ in pro_lst:
#             if (nx, ny) == (px, py):
#                 return False
#     return True

# def dfs(idx, total, connected):
#     global min_len, max_connected, pro_lst

#     if idx == len(pro_lst):
#         if connected > max_connected or (connected == max_connected and total < min_len):
#             max_connected = connected
#             min_len = total
#             print(pro_lst)
#         return
    
#     if connected + len(pro_lst) - idx < max_connected:
#         return
    
#     x, y = pro_lst[idx][0], pro_lst[idx][1]
    
#     if x == 0 or x == N - 1 or y == 0 or y == N - 1:
#         dfs(idx + 1, total, connected + 1)
#         return

#     dfs(idx + 1, total, connected)

#     for i in range(4):
#         chk_lst = [x, y, i]
#         if chk(chk_lst, pro_lst[:idx] + pro_lst[idx+1:]):
#             length = chk_len(chk_lst)
#             pro_lst[idx][2] = i
#             dfs(idx + 1, total + length, connected + 1)
#             pro_lst[idx][2] = -1  # 방향 초기화

# for test_case in range(1, T+1):
#     N = int(input())
#     lst = [list(map(int,input().split())) for _ in range(N)]
#     pro_lst = []
#     min_len = float('inf')
#     max_connected = 0

#     for i in range(N):
#         for j in range(N):
#             if lst[i][j] == 1:
#                 pro_lst.append([i,j,-1])

#     dfs(0, 0, 0)

#     print(f'#{test_case} {min_len}')

# pro_lst 대신 cores를 사용:
# cores는 단순히 코어의 위치 (x, y)만 저장합니다.
# 이전 코드에서 방향 정보를 저장하려던 시도를 제거했습니다.

# is_valid_path 함수 추가:
# 특정 방향으로의 경로가 유효한지 확인합니다.
# 이전의 chk 함수를 대체합니다.

# connect_core 함수 추가:
# 코어를 특정 방향으로 연결하거나 연결을 해제합니다.
# 연결된 길이를 반환합니다.

# dfs 함수 수정:
# pro_lst를 직접 수정하는 대신 lst 보드를 수정합니다.
# 각 방향에 대해 연결을 시도하고, 백트래킹을 위해 연결을 해제합니다.

# chk_len 함수 수정:
# 이제 x, y, direction을 직접 받아 길이를 계산합니다.
# 이러한 변경으로 코드의 로직이 더 명확해지고, 의도한 대로 작동할 것입니다. 
# 이제 각 코어에 대해 모든 가능한 연결 방법을 탐색하며, 
# 최대한 많은 코어를 연결하면서 최소 길이를 찾을 것입니다.