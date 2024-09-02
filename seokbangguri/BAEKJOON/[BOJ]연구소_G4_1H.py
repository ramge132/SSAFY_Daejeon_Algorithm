from itertools import combinations
from collections import deque

# 상 하 좌 우
dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
# 바이러스 확산
def virus_bfs(matrix, queue):
    global result
    temp_virus = 0
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 영역을 벗어 난 경우
            if not (0 <= nx <= M-1 and 0 <= ny <= N-1):
                continue

            # 벽이거나 바이러스가 있는 경우
            elif matrix[ny][nx] != 0:
                continue

            # 빈 공간이 있는 경우
            else:
                matrix[ny][nx] = 2
                temp_virus += 1
                queue.append((nx, ny))
    
    if result < safe_count - temp_virus:
        result = safe_count - temp_virus

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
can_build = []
virus_pos = []
walls_count = 0
safe_count = N * M
result = 0

for y in range(N):
    for x in range(M):
        # 빈 공간
        if lab[y][x] == 0:
            can_build.append((x, y))
            continue
        # 바이러스
        elif lab[y][x] == 2:
            virus_pos.append((x, y))
            safe_count -= 1
        # 벽
        else:
            walls_count += 1
            safe_count -= 1

safe_count -= 3

for c in list(combinations(can_build, 3)):
    copy_lab = [a[:] for a in lab]
    spread_pos = deque([])
    for pos in virus_pos:
        spread_pos.append(pos)

    for i in range(3):
        x, y = c[i]
        copy_lab[y][x] = 1
        walls_count += 1
    
    virus_bfs(copy_lab, spread_pos)

print(result)
