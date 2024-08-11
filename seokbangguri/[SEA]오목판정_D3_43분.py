# 시작 20:30 21:13
import sys
sys.stdin = open('../../input.txt')

# 수평, 수직
def verhor(i, mtx):
    for idx in range(N-4):
        if len(set(mtx[i][idx:idx+5])) == 1 and mtx[i][idx] == 'o':
            return True
    return False

# # 대각
# def dia(x, y, mtx):
#     global result
#     for i in range(5):
#         if mtx[y+i][x+i] == '.':
#             return False
#     result = True
#     return True

# 대각
def dia(x, y, mtx):
    # 좌상->우하 대각선 체크
    if all(mtx[y+i][x+i] == 'o' for i in range(5)):
        return True
    # 우상->좌하 대각선 체크
    if all(mtx[y+i][x+4-i] == 'o' for i in range(5)):
        return True
    return False

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    zip_matrix = list(zip(*matrix))
    reversed_matrix = list(reversed(matrix))
    result = False

    # 수직, 수평 체크
    for x in range(N):
        if verhor(x, zip_matrix) or verhor(x, matrix):
            result = True
            break

    if result:
        print(f'#{test_case} YES')
        continue

    # 대각 체크
    for y in range(N-4):
        for x in range(N-4):
            if dia(x, y, matrix) or dia(x, y, reversed_matrix):
                result = True
                break
        if result:
            break

    if result:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
