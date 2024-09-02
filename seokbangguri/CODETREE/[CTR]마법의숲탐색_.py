from collections import deque
from pprint import pprint

# 상 우 하 좌
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# 정령 탈출
def bfs(queue):
    visited = [[False]*c for _ in range(r)]
    max_y = 0
    while queue:
        x, y = queue.popleft()

        pass

def draw_cross_line(pos, no, direction):
    cx, cy = pos
    forest[cy][cx] = no
    for i, (dx, dy) in enumerate(dxy):
        if i == direction:
            forest[cy + dy][cx + dx] = -1 * no
            continue
        forest[cy + dy][cx + dx] = no


# 밑으로 내려갈 수 있는지 확인하는 함수
def check_down(position, rotateTime = 0):
    x, y = position
    # 아래로 내려갈 수 있는 경우
    if y+2 < r and forest[y+1][x-1] == 0 and forest[y+1][x+1] == 0 and forest[y+2][x] == 0:
        return check_down((x, y+1))
    
    # 아래로 내려갈 수 없는 경우
    else:
        if y == r-2:
            return position, rotateTime
        return check_left((x, y), rotateTime)
    
# 왼쪽으로 갈 수 있는지 확인하는 함수
def check_left(position, rotateTime):
    x, y = position
    # 왼쪽으로 갈 수 있는 경우
    if x-2 >= 0 and y+2 < r and forest[y-1][x-1] == 0 and forest[y][x-2] == 0 and forest[y+1][x-1] == 0 and forest[y+1][x-2] == 0 and forest[y+2][x-1] == 0:
        return check_down((x-1, y+1), rotateTime-1)
    # 왼쪽으로 갈 수 없는 경우
    else:
        return check_right((x, y), rotateTime)

# 오른쪽으로 갈 수 있는지 확인하는 함수
def check_right(position, rotateTime):
    x, y = position
    # 오른쪽으로 갈 수 있는 경우
    if x+2 < c and y+2 < r and forest[y-1][x+1] == 0 and forest[y][x+2] == 0 and forest[y+1][x+1] == 0 and forest[y+1][x+2] == 0 and forest[y+2][x+1] == 0:
        return check_down((x+1, y+1), rotateTime+1)
    # 오른쪽으로 갈 수 없는 경우
    else:
        return (x, y), rotateTime

# 골렘이 스폰되고 움직일 수 있는지 확인하는 함수
def movingMonster(x_pos, direction, no):
    global result, forest
    # 처음 골렘이 숲으로 들어올 수 있는지 확인
    # 못 들어오는 경우 숲 초기화
    '''
    
    낙하 후 셀 안에 못 들어온 경우 좌, 우로 굴러서 셀 안에 들어올 수 있으면 스폰 가능

    '''
    if forest[0][x_pos-1:x_pos+2].count(0) != 3 or forest[1][x_pos-1:x_pos+2].count(0) != 3 or forest[2][x_pos] != 0:
        forest = [[0]*c for _ in range(r)]

    # 가능 한 경우
    else:
        (mon_pos_x, mon_pos_y), rotate_time = check_down((x_pos, 1))
        '''
        
        조건문 추가 y 값이 3보다 작은 경우 맵 초기화
        '''
        if rotate_time < -4:
            direction += rotate_time + abs(rotate_time)//4 * 4
        elif rotate_time > 4:
            direction -= rotate_time - abs(rotate_time)//4 * 4
        else: direction += rotate_time
        # 숲에 골렘 위치 추가
        draw_cross_line((mon_pos_x, mon_pos_y), no, direction)

        # frog_pos = deque([(mon_pos_x, mon_pos_y)])
        # # 정령 탈출
        # result += bfs(frog_pos)
        '''
        
        수정 중
        
        '''





r, c, k = map(int, input().split())
monsters = [list(map(int, input().split())) for _ in range(k)]
forest = [[0]*c for _ in range(r+3)]
result = 0

for i, (x, d) in enumerate(monsters, start=1):
    movingMonster(x-1, d, i)
    print('골렘 번호', i)
    pprint(forest)


           

