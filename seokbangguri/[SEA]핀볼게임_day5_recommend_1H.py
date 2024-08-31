import sys
sys.stdin = open('./04_algorithm/day_5/swea_5650/input.txt')
# sys.stdin = open('input.txt')

# 0: 상, 1: 좌, 2: 하, 3: 우
dxy = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def changeDirection(block_shape, direction):
    if block_shape == 1:
        if direction == 2:
            return 3
        elif direction == 1:
            return 0
    elif block_shape == 2:
        if direction == 1:
            return 2
        elif direction == 0:
            return 3
    elif block_shape == 3:
        if direction == 3:
            return 2
        elif direction == 0:
            return 1
    elif block_shape == 4:
        if direction == 3:
            return 0
        elif direction == 2:
            return 1
        
    return (direction + 2)%4

def simulation(position):
    global best_score

    for direction, (dx, dy) in enumerate(dxy):
        cx, cy = position
        temp_score = 0

        while True:
            nx, ny = cx + dx, cy + dy
            # 출발지로 돌아온 경우
            if (nx, ny) == position:
                if temp_score > best_score:
                    best_score = temp_score
                break
                
            # 다음 블럭 확인
            # 영역 밖으로 나가는 경우 (벽을 만나는 경우)
            if not (0 <= nx <= N-1 and 0 <= ny <= N-1):
                direction = (direction + 2)%4
                dx, dy = dxy[direction]
                temp_score += 1
            
            # 블럭을 만나는 경우
            elif 1 <= pinball[ny][nx] <= 5:
                direction = changeDirection(pinball[ny][nx], direction)
                dx, dy = dxy[direction]
                temp_score += 1

            # 웜홀을 만나는 경우
            elif 6 <= pinball[ny][nx] <= 10:
                for worm_pos in worm_hole[pinball[ny][nx]]:
                    if worm_pos != (nx, ny):
                        nx, ny = worm_pos
                        break

            # 블랙홀을 만나는 경우
            elif pinball[ny][nx] == -1:
                if temp_score > best_score:
                    best_score = temp_score
                break
            
            cx, cy = nx, ny
            
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pinball = [list(map(int, input().split())) for _ in range(N)]
    start_points = []
    worm_hole = {}

    best_score = 0

    for y in range(N):
        for x in range(N):
            # 시작점 가능
            if pinball[y][x] == 0:
                start_points.append((x, y))
            # 웜홀 좌표 저장
            elif 6 <= pinball[y][x] <= 10:
                # 키 없을 때
                if not worm_hole.get(pinball[y][x]):
                    worm_hole[pinball[y][x]] = [(x, y)]
                else:
                    worm_hole[pinball[y][x]].append((x, y))


    for start_point in start_points:
        simulation(start_point)

    print(f'#{test_case} {best_score}')