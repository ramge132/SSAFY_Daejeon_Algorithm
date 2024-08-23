"""
# 문제 링크
- https://www.acmicpc.net/problem/13460

# 문제 설명:
| 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다. 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다. 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다. 이때, 파란 구슬이 구멍에 들어가면 안 된다. 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다. 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다. 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다. 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다. 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.

# 접근법:
- 바로 DFS가 떠올라 해당 방식으로 접근을 진행했습니다.
- 이 문제에서 개인적으로 생각하는 키 포인트는 중력으로 인해 움직이기 때문에, **겹치는 공**을 어떻게 처리할 것인가라고 생각합니다.
    - 해당 부분은 코드 상에서 *빨간 공과 파란 공이 겹쳐서 존재한다. 이렇게 되면 이전 전후 관계를 따진다.* 주석 부분에 작성을 했습니다.
- 시도 횟수가 10번까지라 완탐이 문제 없다고 생각했는데, 랩탑에서 돌리니 실행시간이 길어 다음과 같은 방식을 사용했습니다.
    1. 특정 방향으로 움직였는데도 공의 위치가 변화 없다. 이는 게임 자체에 의미없는 행동이기 때문에 해당 위치와 액션에서 DFS를 돌리지 않았습니다.
    2. 이미 shortest path를 찾았다면 이것보다 긴 것을 찾을 필요는 없다.
- 또한, 두 공이 동시에 들어갈 수 있기 때문에, 종료 조건은 파란 공이 먼저 빠질 때로 선택했습니다.
"""

DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]]


shortest_path = float('inf')
def DFS(game_board, current_RB_loc, depth):
    global shortest_path

    if depth > shortest_path:
        return -1
    if depth > 10:
        return -1
    if game_board[current_RB_loc[1][0]][current_RB_loc[1][1]] == "O":
        # 파란 공이 들어갔다!
        return -1
    if game_board[current_RB_loc[0][0]][current_RB_loc[0][1]] == "O":
        # 빨간 공이 들어갔다!
        if shortest_path > depth:
            shortest_path = depth
        return depth

    for idx, direction in enumerate(DIRECTION):
        dx, dy = direction

        temp_current_RB_loc = []
        for i in range(2):
            temp_x, temp_y = current_RB_loc[i][0], current_RB_loc[i][1]

            while game_board[temp_x][temp_y] == ".":
                # move straight
                temp_x, temp_y = temp_x + dx, temp_y + dy
            if game_board[temp_x][temp_y] == "#":
                temp_x, temp_y = temp_x - dx, temp_y - dy
            temp_current_RB_loc.append((temp_x, temp_y))
        
        if (temp_current_RB_loc[0] == temp_current_RB_loc[1]) and game_board[temp_current_RB_loc[0][0]][temp_current_RB_loc[0][1]] != "O":
            # 빨간 공과 파란 공이 겹쳐서 존재한다. 이렇게 되면 이전 전후 관계를 따진다.
            jud = -1
            if idx == 0:
                if current_RB_loc[0][0] > current_RB_loc[1][0]: jud = 0
                else: jud = 1
            elif idx == 1:
                if current_RB_loc[0][0] > current_RB_loc[1][0]: jud = 1
                else: jud = 0
            elif idx == 2:
                if current_RB_loc[0][1] > current_RB_loc[1][1]: jud = 0
                else: jud = 1
            elif idx == 3:
                if current_RB_loc[0][1] > current_RB_loc[1][1]: jud = 1
                else: jud = 0
            temp_current_RB_loc[jud] = (temp_current_RB_loc[jud][0] - dx, temp_current_RB_loc[jud][1] - dy)
        if current_RB_loc == temp_current_RB_loc:
            continue
        else:
            DFS(game_board, temp_current_RB_loc, depth+1)
                    

N, M = list(map(int, input().split()))

game_board = []
R_loc = None
B_loc = None
for n_iter in range(N):
    # 빨간 공과 파란 공은 좌표로만 생각하자
    input_line = input()
    temp_line = ""
    for idx, c in enumerate(input_line):
        if c == "B":
            temp_line += "."
            B_loc = (n_iter, idx)
        elif c == "R":
            temp_line += "."
            R_loc = (n_iter, idx)
        else:
            temp_line += c
    game_board.append(temp_line)

DFS(game_board, [R_loc, B_loc], 0)

if shortest_path == float('inf'):
    print(-1)
else:
    print(shortest_path)