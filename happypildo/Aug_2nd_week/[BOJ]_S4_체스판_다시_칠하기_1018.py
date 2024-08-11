"""
# 문제 설명
- 1*1 정사각형의 흰색 또는 검은색으로 구성된 N*M 나무 판이 주어진다.
- 이를 8*8로 쪼개서 체스 판을 만들려고 하는데, 색이 뒤죽박죽이라 다시 칠할 부분은 칠해야 한다. (체스판처럼)
- 자르는 경우의 수 중, 색을 최소한으로 칠할 수 있는 횟수는 몇인가?

# 해피필도 팁
- 입력 최대 사이즈가 50이라서 상남자식 `O(N^4)`으로 승부를 봤다.
- 최대 연산 횟수는 거의 50^4 = 6,250,000이라서 널널하다고 생각했다.
"""
CHESS = 8


def start_with_white_or_black(cut_board):
    paint_count_W = 0
    paint_count_B = 0

    prev_color_start_with_W = 'B'
    prev_color_start_with_B = 'W'
    for i in range(CHESS):
        for j in range(CHESS):
            if cut_board[i][j] == prev_color_start_with_W:
                paint_count_W += 1
            if prev_color_start_with_W == 'B':
                prev_color_start_with_W = 'W'
            else:
                prev_color_start_with_W = 'B'

            if cut_board[i][j] == prev_color_start_with_B:
                paint_count_B += 1
            if prev_color_start_with_B == 'B':
                prev_color_start_with_B = 'W'
            else:
                prev_color_start_with_B = 'B'
        if prev_color_start_with_W == 'B':
                prev_color_start_with_W = 'W'
        else:
            prev_color_start_with_W = 'B'
        if prev_color_start_with_B == 'B':
            prev_color_start_with_B = 'W'
        else:
            prev_color_start_with_B = 'B'
    
    return min(paint_count_W, paint_count_B)

N, M = list(map(int, input().split()))
board = [input() for n_iter in range(N)]

answer = float('inf')
for i in range(N - CHESS + 1):
    for j in range(M - CHESS + 1):
        new_board = [board[temp_i][j:j+CHESS] for temp_i in range(i, i+CHESS)]
        answer = min(answer, start_with_white_or_black(new_board))

print(answer)
