dxy = [[-1,0],[1,0],[0,-1],[0,1]]
def find_route(x, y):
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if maze[ny][nx] == 0:
            maze[ny][nx] = 1
            if find_route(nx, ny) == 1:
                return 1
        elif maze[ny][nx] == 3:
            return 1
    return 0

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f'#{t} {find_route(1,1)}')
    # ///////////////////////////////////////////////////////////////////////////////////
