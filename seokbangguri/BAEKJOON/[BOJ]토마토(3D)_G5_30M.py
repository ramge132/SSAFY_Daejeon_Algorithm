# 위 아래 좌 우 하 상
dxyz = [[0, 0, 1], [0, 0, -1], [-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0]]


def bfs(fucking_next_tomatoooooooo):
    global tomato_cnt

    # 이번 턴이 끝나고 익을 토마토 좌표
    tomato = set()

    while fucking_next_tomatoooooooo:
        cx, cy, cz = fucking_next_tomatoooooooo.pop()

        # 6방향 탐색
        for dx, dy, dz in dxyz:
            nx, ny, nz = cx + dx, cy + dy, cz + dz
            
            # 다음 좌표가 영역을 벗어나는 경우
            if not (0<= nx <=M-1 and 0<= ny <= N-1 and 0<= nz <=H-1):
                continue

            # 다음 좌표가 이미 익은 토마토이거나 빈 곳이거나 이미 탐색한 익을 토마토인 경우
            np = trays[nz][ny][nx]
            if np == 1 or np == -1 or (nx, ny, nz) in tomato:
                continue

            # 익을 토마토에 추가
            trays[nz][ny][nx] = 1
            tomato_cnt += 1
            tomato.add((nx, ny, nz))

    return tomato


M, N, H = map(int, input().split())

trays = [list(list(map(int, input().split())) for _ in range(N)) for _ in range(H)]
time = -1
starting_tomato_positions = set()
tomato_cnt = 0
empty_cnt = 0

for z in range(H):
    for y in range(N):
        for x in range(M):
            if trays[z][y][x] == 1:
                # 초기 탐색 돌릴 토메이러 위치
                starting_tomato_positions.add((x, y, z))
                tomato_cnt += 1
            elif trays[z][y][x] == -1:
                empty_cnt += 1

while starting_tomato_positions:
    time += 1
    next_tomato = bfs(starting_tomato_positions)
    starting_tomato_positions = next_tomato

if M * N * H == tomato_cnt + empty_cnt:
    print(time)
else:
    print(-1)