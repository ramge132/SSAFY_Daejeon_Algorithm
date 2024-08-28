from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def bfs(queue, times):
    global have_to_be_done
    length = len(queue)
    temp_length = 0

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            # 범위를 벗어난 경우
            if not (0 <= nx <= M-1 and 0 <= ny <= N-1):
                continue

            # 덜익은 경우
            if tray[ny][nx] == 0:
                tray[ny][nx] = 1
                have_to_be_done -= 1

                # 다 익은 경우
                if not have_to_be_done:
                    return print(times)

                queue.append((nx, ny))
                temp_length += 1
        
        length -= 1

        if not length:
            times += 1
            length += temp_length
            temp_length = 0
        
        
    if have_to_be_done:
        return print(-1)
    else:
        return print(times)


M, N = map(int, input().split())
tray = [list(map(int, input().split())) for _ in range(N)]
done = deque([])
have_to_be_done = 0

for y in range(N):
    for x in range(M):
        if tray[y][x] == 1:
            done.append((x, y))
        elif tray[y][x] == 0:
            have_to_be_done += 1

if have_to_be_done == 0: print(0)
else: bfs(done, 1)