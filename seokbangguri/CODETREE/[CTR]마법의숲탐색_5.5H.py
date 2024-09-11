from collections import deque

# 상 우 하 좌
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

# 정령 탈출
def bfs(queue):
    visited = [[False]*c for _ in range(r+3)]
    max_y = 0
    while queue:
        cx, cy = queue.popleft()

        if visited[cy][cx]:
            continue

        visited[cy][cx] = True

        # 최대 y값 바꿔주기
        if cy > max_y:
            max_y = cy

        # 이미 최대 y값이면 리턴
        if max_y == r+2:
            return max_y - 2

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            # 범위 밖으로 나감
            if not (0 <= nx <= c-1 and 3 <= ny <= r+2):
                continue
            
            # 골렘이 아님
            if forest[ny][nx] == 0:
                continue

            # 같은 골렘 위 돌아 다닐 때
            if abs(forest[cy][cx]) == abs(forest[ny][nx]):
                # 이미 방문 한 곳이면 패스
                if not visited[ny][nx]:
                    queue.append((nx, ny))


            # 다른 골렘인 경우 현재 위치가 출구여야 가능함
            elif forest[cy][cx] < 0 and forest[ny][nx] != abs(forest[cy][cx]):
                # 이미 방문 한 곳이면 패스
                if not visited[ny][nx]:
                    queue.append((nx, ny))


    return max_y - 2


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
    if y+2 < r+3 and forest[y+1][x-1] == 0 and forest[y+1][x+1] == 0 and forest[y+2][x] == 0:
        return check_down((x, y+1), rotateTime)
    
    # 아래로 내려갈 수 없는 경우
    else:
        if y == r+1:
            return position, rotateTime
        return check_left((x, y), rotateTime)
    
    
# 왼쪽으로 갈 수 있는지 확인하는 함수
def check_left(position, rotateTime):
    x, y = position
    # 왼쪽으로 갈 수 있는 경우
    if x-2 >= 0 and y+2 < r+3 and forest[y-1][x-1] == 0 and forest[y][x-2] == 0 and forest[y+1][x-1] == 0 and forest[y+1][x-2] == 0 and forest[y+2][x-1] == 0:
        return check_down((x-1, y+1), rotateTime-1)
    # 왼쪽으로 갈 수 없는 경우
    else:
        return check_right((x, y), rotateTime)
    

# 오른쪽으로 갈 수 있는지 확인하는 함수
def check_right(position, rotateTime):
    x, y = position
    # 오른쪽으로 갈 수 있는 경우
    if x+2 < c and y+2 < r+3 and forest[y-1][x+1] == 0 and forest[y][x+2] == 0 and forest[y+1][x+1] == 0 and forest[y+1][x+2] == 0 and forest[y+2][x+1] == 0:
        return check_down((x+1, y+1), rotateTime+1)
    # 오른쪽으로 갈 수 없는 경우
    else:
        return (x, y), rotateTime
    

# 골렘이 스폰되고 움직일 수 있는지 확인하는 함수
def movingMonster(x_pos, direction, no):
    global result, forest
    # 처음 골렘이 숲으로 들어올 수 있는지 확인
    # 못 들어오는 경우 숲 초기화

    (mon_pos_x, mon_pos_y), rotate_time = check_down((x_pos, 1))
    # 셀 안에 들어올 수 없음
    if mon_pos_y <= 3:
        forest = [[0]*c for _ in range(r+3)]
        
    else:
        direction = (direction + rotate_time) % 4

        # 숲에 골렘 위치 추가
        draw_cross_line((mon_pos_x, mon_pos_y), no, direction)

        frog_pos = deque([(mon_pos_x, mon_pos_y)])
        # 정령 탈출
        result += bfs(frog_pos)


r, c, k = map(int, input().split())
monsters = [list(map(int, input().split())) for _ in range(k)]
forest = [[0]*c for _ in range(r+3)]
result = 0

for i, (x, d) in enumerate(monsters, start=1):
    movingMonster(x-1, d, i)

print(result)