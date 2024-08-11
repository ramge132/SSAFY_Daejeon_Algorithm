"""
# 문제 설명
- 체스판이 있고, 그 위에 킹과 돌이 있다.
- 킹은 움직일 수 있는 여러 방향이 있는데, 움직이려는 곳에 돌이 있다면 돌을 움직이는 방향으로 밀어내고 간다.
- 킹과 돌의 초기 위치와 N개의 명령이 주어질 때, 최종적으로 킹과 돌의 위치는 어디인가?
    - 여기서, 위치는 C3과 같이 주어진다. (체스판 형태로)

# 접근 방법
- 인덱싱 연습하기 좋은 문제라고 생각한다. 나는 체스판과 이동 방향을 왼쪽으로 돌려서 구현했다.
- 킹을 움직이면서 돌의 위치를 계속해서 확인해야 하기 때문에, 구현으로 풀었다.
"""
DIRECTION = {
    'R': [1, 0],
    'L': [-1, 0],
    'B': [0, -1],
    'T': [0, 1],
    'RT': [1, 1],
    'LT': [-1, 1],
    'RB': [1, -1],
    'LB': [-1, -1]
}

ALPHA_TO_INT = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8
}

CHESS_SIZE = 8


loc_king, loc_stone, N = input().split()

for n_iter in range(int(N)):
    order = input()

    dx, dy = DIRECTION[order]
    
    king_x, king_y = ALPHA_TO_INT[loc_king[0]], int(loc_king[1])
    stone_x, stone_y = ALPHA_TO_INT[loc_stone[0]], int(loc_stone[1])

    king_temp_x, king_temp_y = ALPHA_TO_INT[loc_king[0]] + dx, int(loc_king[1]) + dy
    if (0 < king_temp_x < CHESS_SIZE + 1) and (0 < king_temp_y < CHESS_SIZE + 1):
        # 움직일 수 있다.
        if (king_temp_x == stone_x) and (king_temp_y == stone_y):
            # king이 가려는 곳에 돌이 있다면, 돌을 밀어내자.
            temp_stone_x, temp_stone_y = stone_x + dx, stone_y + dy
            if (0 < temp_stone_x < CHESS_SIZE + 1) and (0 < temp_stone_y < CHESS_SIZE + 1):
                # 돌이 넘어가지 않는다. 위치 업데이트
                loc_king = list(ALPHA_TO_INT.keys())[king_temp_x - 1] + str(king_temp_y)
                loc_stone = list(ALPHA_TO_INT.keys())[temp_stone_x - 1] + str(temp_stone_y)
            else:
                # 돌이 넘어간다. 위치 업데이트 하지 말자
                continue
        else:
            # 가려는 곳에 돌이 없고, 갈 수 있다. 위치 업데이트
            loc_king = list(ALPHA_TO_INT.keys())[king_temp_x - 1] + str(king_temp_y)
            loc_stone = list(ALPHA_TO_INT.keys())[stone_x - 1] + str(stone_y)
    else:
        # 킹이 가려는 곳이 범위를 벗어날 경우, 해당 order를 무시한다.
        continue

print(loc_king)
print(loc_stone)

