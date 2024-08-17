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
