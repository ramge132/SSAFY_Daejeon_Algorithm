# 십자모양 중앙 포함 5칸
# 4칸중 한칸 골렘의 출구
# 다음 위치 걸리는 것 없어야 함
# 서쪽 방향으로 회전하여 이동
# 서쪽 이동, 아래쪽 이동
# R 행, C 열


# 골렘이 더이상 남쪽으로 갈 수 없는 상태일 때, 다른 골렘 먼저 이동
# 더이상 아래로 못갈 때, lst에 1로 설치한다.


# 빈공간 0
# 이동 불가 1
# 골렘 2

from pprint import pprint
from collections import deque

def is_valid(i, j):
    return 0 <= i < C and 0 <= j < R

def set_gol(i, j):
    global lst
    # 5개
    # i - 1 j
    # i j - 1 /  i j / i j + 1
    # i + 1 j

    # zz
    # 검사를 한 이후에 동작하니까 상관 없음

    if is_valid(i - 1, j): lst[i - 1][j] = 1
    if is_valid(i, j - 1): lst[i][j -1] = 1
    if is_valid(i, j): lst[i][j] = 1
    if is_valid(i, j + 1): lst[i][j + 1] = 1
    if is_valid(i+ 1, j): lst[i + 1][j] = 1


def chk_down(i, j):
    if is_valid(i + 2, j) and is_valid(i + 1, j - 1) and is_valid(i + 1, j + 1):
        return lst[i+2][j] == 0 and lst[i + 1][j - 1] == 0 and lst[i + 1][j + 1] == 0
    else:
        return False
    
def chk_left(i,j):
    if is_valid(i-1,j - 1) and is_valid(i, j - 2) and is_valid(i + 1, j - 1):
        return lst[i-1][j-1] == 0 and lst[i][j -2] == 0 and lst[i+1][j-1] == 0
    else:
        return False

def chk_right(i,j):
    if is_valid(i - 1, j + 1) and is_valid(i, j + 2) and is_valid(i + 1, j + 1):
        return lst[i - 1][j + 1] == 0 and lst[i][j + 2] == 0 and lst[i + 1][j + 1] == 0
    else:
        return False


def down(i, j, dir):
    global lst, result
    print(i, j, dir)
    pprint(lst)

    if not chk_down(i, j):
        if i == C - 2: # 바닥에 도달했을 때,
            print('reached')
            result += C - 3
            set_gol(i, j)
            return
        
        print('chk')

        if chk_left(i, j):
            if dir == 0:
                dir = 4
            if chk_down(i, j - 1):
                down(i, j - 1, dir  - 1)
                return

            else:
                print('---------left pass--------')
                print(dir)
                if i < 4:
                    print('---------over col--------')
                    lst = [[0] * R for _ in range(C)]
                    return
                
                if dir == 0 or dir == 4:
                    if bfs(i - 1, j):
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return

                elif dir == 1:

                    if bfs(i, j + 1):    
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return

                elif dir == 2:
                    if bfs(i + 1, j):
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return
                
                elif dir == 3:
                    if bfs(i, j - 1):
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return

        if chk_right(i, j):
            if chk_down(i, j + 1):
                print('right_chk')
                down(i, j + 1, (dir + 1) % 4)
                return
            
            else:
                if i < 4:
                    print('---------over col--------')
                    lst = [[0] * R for _ in range(C)]
                return
                print('---------right pass--------')

                if dir == 0:
                    if bfs(i - 1, j):
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return

                elif dir == 1:
                    if bfs(i, j + 1):    
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return

                elif dir == 2:
                    if bfs(i + 1, j):
                        result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return
                
                elif dir == 3:
                    if bfs(i, j - 1):
                       result += C - 3
                    else:
                        result += i - 1
                    set_gol(i, j)
                    return
        
        else:

            if i < 4:
                print('---------over col--------')
                lst = [[0] * R for _ in range(C)]
                return
            
            print('---------not matched--------')

            if dir == 0:
                if bfs(i - 1, j):
                    result += C - 3
                else:
                    result += i - 1
                set_gol(i, j)
                return

            elif dir == 1:
                if bfs(i, j + 1):
                    result += C - 3
                else:
                    result += i - 1
                set_gol(i, j)
                return

            elif dir == 2:
                if bfs(i + 1, j):
                    result += C - 3
                else:
                    result += i - 1
                set_gol(i, j)
                return
            
            elif dir == 3:
                if bfs(i, j - 1):
                    result += C - 3
                else:
                    result += i - 1
                set_gol(i, j)
                return

            # 나갈 수 있는지 탐색

    else:
        print('down_chk')
        down(i + 1, j, dir)

    # 3방향 탐색을 했는데 전부 못갈 때,
    # 최종 결정

def bfs(i, j):
    queue = deque([(i ,j)])

    while queue:
        x, y = queue.popleft()
        for dx, dy in DXY:
            nx, ny = x + dx, y + dy
            if nx == C - 2:
                return True
            if not is_valid(nx, ny): return
            if lst[nx][ny] == 1:
                queue.append((nx, ny))
    
    return False


DXY = [(1,0), (0,1), (0, -1)] # 상 우 좌

C, R, K = map(int, input().split())
C += 3
lst = [[0] * R for _ in range(C)]

# 골렘의 출발 열
# 해당 골렘의 출구 방향
result = 0
gol = []

for i in range(K):
    a, b = map(int, input().split())
    gol.append((a, b))

for i in range(len(gol)):
    print(f'--------------next {i}-----------')
    down(1, gol[i][0] - 1, gol[i][1])
    print(f'{i} {result}')


# print(gol)
print(result)
pprint(lst)