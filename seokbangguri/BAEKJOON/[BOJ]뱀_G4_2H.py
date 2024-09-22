from collections import deque

# 상 우 하 좌
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def snakeMoving(snake, direction=1):
    time = 0
    while True:
        dx, dy = dxy[direction]
        cx, cy = snake[0]
        nx, ny = cx + dx, cy + dy


        if change_directions and change_directions[0][0] == str(time+1):
            next_direction = change_directions.popleft()
            if next_direction[1] == 'D':
                direction += 1
            else:
                direction += 3
            direction %= 4
        

        # 빈 공간인 경우
        if game_map[ny][nx] == 0:
            snake.appendleft((nx, ny))
            game_map[ny][nx] = 1
            tx, ty = snake.pop()
            game_map[ty][tx] = 0
            time += 1
            continue

        # 사과 만난 경우
        elif game_map[ny][nx] == 2:
            snake.appendleft((nx, ny))
            game_map[ny][nx] = 1
            time += 1
            continue

        # 자기 자신 또는 벽 만난 경우
        elif game_map[ny][nx] == 1:
            return time+1


# 빈 칸은 0, 뱀은 1, 사과는 2
N = int(input())
game_map = [[1]*(N+2)]
for _ in range(N):
    game_map.append([1]+[0]*N+[1])
game_map.append([1]*(N+2))
game_map[1][1] = 1


K = int(input())
for _ in range(K):
    ax, ay = map(int, input().split())
    game_map[ax][ay] = 2


L = int(input())
change_directions = deque([tuple(input().split()) for _ in range(L)])


print(snakeMoving(deque([(1,1)])))