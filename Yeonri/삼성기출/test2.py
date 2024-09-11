from collections import deque
from pprint import pprint

DXY = [(-1, 0), (0, 1), (1, 0), (0, -1),] # 상 우 하 좌

def is_valid(i, j):
    return 0 <= i < R and 0 <= j < C

def chk_down(i, j):
    if is_valid(i + 1, j - 1) and is_valid(i + 1, j + 1) and is_valid(i + 2, j):
        return lst[i + 1][j - 1] == 0 and lst[i + 1][j + 1] == 0 and lst[i + 2][j] == 0
    return False

def chk_left(i, j):
    if is_valid(i, j - 2) and is_valid(i - 1, j - 1) and is_valid(i + 1, j - 1):
        return lst[i][j -2] == 0 and lst[i + 1][j - 1] == 0 # and lst[i - 1][j - 1] == 0
    return False

def chk_right(i, j):
    if is_valid(i, j + 2) and is_valid(i - 1, j + 1) and is_valid(i + 1, j + 1):
        return lst[i][j + 2] == 0 and lst[i + 1][j + 1] == 0 # and lst[i - 1][j + 1] == 0
    return False

def set_gol(i, j, dir):
    global lst

    lst[i + 1][j] = count
    lst[i - 1][j] = count
    lst[i][j - 1] = count
    lst[i][j + 1] = count
    lst[i][j] = count

    init_x, init_y = i + DXY[dir][0], j + DXY[dir][1] # 초기 좌표 설정
    lst[init_x][init_y] = count * 2000

    

def bfs(i, j, dir):
    global lst
    
    init_x, init_y = i + DXY[dir][0], j + DXY[dir][1] # 초기 좌표 설정
    lst[init_x][init_y] = count * 2000
    
    queue = deque([(init_x, init_y)])
    visited = set()
    max_depth = init_x


    while queue:
        print(queue)
        x, y = queue.popleft()
        
        if x == R - 2: # 제일 아래에 도달함
            print(f' bfs -------------- {i} {j} --------------')
            return R
        
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if (nx, ny) in visited: continue
            if not is_valid(nx, ny): continue # 범위 벗어남
            if lst[nx][ny] == 0: continue # 1이 아님
            # 현재 값이 E and 다음 값 != 0
            # 다음 값이 E > 이동 해야 함 > 
            
            print(lst[nx][ny])
            if lst[x][y] == lst[nx][ny] or lst[nx][ny] == lst[x][y] * 2000 or lst[x][y] % 2000 == 0: # 출구일 때, 혹은 같은 숫자를 가질 떄,
                visited.add((nx, ny)) # 방문 추가
                max_depth = max(max_depth, nx)
                queue.append((nx, ny))

    print(max_depth)
    return max_depth

# 내려가는 함수
def down(i, j, dir):
    global result, lst
    #pprint(lst)
    # print(f'---{i} {j} {dir}---')
    if chk_down(i, j):
        down(i + 1, j, dir)
        return
    
    else: #내려갈 수 없을 때,

        if i == R - 2: # 마지막 까지 내려옴
            result += R
            set_gol(i, j, dir)
            return
        
        if chk_left(i, j):
            print('---left chk---')

            if chk_down(i, j - 1):
                if dir == 0:
                    dir = 3
                else:
                    dir -= 1
                down(i + 1, j - 1, dir)
                return
            
            else:
                result += bfs(i + 1, j - 1, dir)
                set_gol(i, j, dir)
                return
        
        if chk_right(i, j):
            dir = (dir + 1) % 4
            
            print('---right chk---')

            if chk_down(i, j + 1):
                down(i + 1, j + 1, dir)
                return
            
            else:
                result += bfs(i + 1, j + 1, dir)
                set_gol(i, j, dir)
                return
        
        if i == 0:
            lst = [[0] * C for _ in range(R)]
            return
        
        else: # 이동 조건을 모두 만족하지 않았을 때,
            result += bfs(i, j, dir)
            set_gol(i, j, dir)
            return


R, C, K = map(int, input().split())

lst = [[0] * C for _ in range(R)]
gol = []
result = 0
count = 1

for _ in range(K):
    gol_j, dir = map(int, input().split())
    gol.append((gol_j, dir))

for gol_j, dir in gol:
    down(0, gol_j - 1, dir)
    count += 1
    print('------------')
    print(gol_j - 1, dir)
    pprint(lst)
    print(f'result: {result}')
    print(f'result: {result}')
    print(f'result: {result}')

print(result)

# 1. 골렘이 내려 갈 수 있는지 확인
# 2. 골렘의 왼쪽 확인 -> 아래 이동 확인
# 3. 골렘의 오른쪽 확인 -> 아래 이동 확인
# 종료 조건
# 더이상 내려갈 수 없을 때
# - 왼쪽 오른쪽으로 이동해서 아래 이동이 불가능한 상황
# - 끝까지 내려갔을 때,
# bfs를 이용해서 탐색 -> 주변에 1이 존재할때, 이동

# bfs 탐색을 할 때, 생각하지 않은 부분
# -> 골렘이 출구를 이용해서 나머지 블록으로 이동할 수 있다. 다른 블록들도 포함을 해야 한다.