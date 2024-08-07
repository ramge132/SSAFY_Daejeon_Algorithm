from collections import deque
# 우, 하, 상, 좌
dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs():
    while len(Q):
        x, y = Q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 매트릭스의 레인지를 넘어가는 경우 진행 X
            n = len(matrix)
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue

            # 현재 탐색의 작업 시간
            cur_min_val = min_val_matrix[y][x] + matrix[ny][nx]

            # 해당 위치까지 최소 시간이 아니면 진행 X (가지치기)
            if min_val_matrix[ny][nx] <= cur_min_val:
                continue
            # 최단 시간 일 경우
            else:
                # 큐에 추가
                Q.append((nx, ny))
                # 최단 시간 업데이트
                min_val_matrix[ny][nx] = cur_min_val


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    matrix = [list(map(int, input())) for _ in range(N)]
    min_val_matrix = [[float('inf')] * N for _ in range(N)]
    Q = deque([(0, 0)])
    min_val_matrix[0][0] = matrix[0][0]
    bfs()
    print(f'#{test_case} {min_val_matrix[-1][-1]}')
    # ///////////////////////////////////////////////////////////////////////////////////
