# https://www.acmicpc.net/problem/9663


def is_safe(board, row, col, N):
    # 이 행의 왼쪽을 검사
    for i in range(col):
        if board[row][i] == 1:
            return False

    # 왼쪽 위 대각선을 검사
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # 왼쪽 아래 대각선을 검사
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    # 모든 열에 퀸을 놓았다면 성공적인 배치로 간주
    if col >= N:
        return 1

    count = 0
    for i in range(N):
        # 현재 위치가 안전한지 확인
        if is_safe(board, i, col, N):
            # 퀸을 현재 위치에 놓기
            board[i][col] = 1
            # 다음 열에 대해 재귀적으로 퀸을 놓기
            count += solve_n_queens(board, col + 1, N)
            # 퀸을 다시 제거 (백트래킹)
            board[i][col] = 0

    return count

def n_queens(N):
    # NxN 크기의 체스판 초기화
    board = [[0] * N for _ in range(N)]
    # 퀸 배치 방법의 수 계산
    return solve_n_queens(board, 0, N)


N = int(input())

print(n_queens(N))
