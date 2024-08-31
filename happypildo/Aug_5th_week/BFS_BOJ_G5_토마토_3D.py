"""
# 문제 설명:
- 본 레포의 "BFS_BOJ_G5_토마토.py"를 참고하길 바란다.
- 본 문제는 위와 아래가 추가된 3D 토마토 판이 주어지는 상황이다.
"""
from collections import deque

DIRECTION = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]


def BFS(H, N, M, tomatos):
    queue = deque()

    # 익은 토마토를 먼저 찾자. 그리고 그걸로 돌리자
    distance_map = [[[float('inf') for m in range(M)] for n in range(N)] for h in range(H)]
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] == 1:
                    # 익은 토마토!
                    queue.append((h, n, m))
                    distance_map[h][n][m] = 0

    # 시간 갱신하기
    while queue:
        z, x, y = queue.popleft()
        
        for direction in DIRECTION:
            dz, dx, dy = direction
            temp_z, temp_x, temp_y = z + dz, x + dx, y + dy
            
            if (-1 < temp_z < H) and (-1 < temp_x < N) and (-1 < temp_y < M):
                if tomatos[temp_z][temp_x][temp_y] != -1:
                    # 토마토다!
                    prev_val = distance_map[temp_z][temp_x][temp_y]
                    incoming_val = distance_map[z][x][y] + 1

                    if prev_val > incoming_val:
                        distance_map[temp_z][temp_x][temp_y] = incoming_val
                        queue.append((temp_z, temp_x, temp_y))
    
    # 토마토가 있던 곳에 익은 토마토로 가득 차 있는가?
    max_distance = -1
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatos[h][n][m] != -1:
                    if distance_map[h][n][m] == float('inf'):
                        return -1
                    else:
                        if max_distance < distance_map[h][n][m]:
                            max_distance = distance_map[h][n][m]
    return max_distance


M, N, H = list(map(int, input().split()))

tomatos = []
for h_iter in range(H):
    tomato_layer = []
    for n_iter in range(N):
        tomato_layer.append(list(map(int, input().split())))
    tomatos.append(tomato_layer)

answer = BFS(H, N, M, tomatos)
print(answer)