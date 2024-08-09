# 풀이 시작 19:20 종료 19:40
import sys
sys.stdin = open('../../input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    # 뒤집은 횟수
    result = 0
    for i in range(N-1, 0, -1):
        # 홀수
        if result%2:
            if matrix[i][0] == i + 1:
                continue
            result += 1
            continue
        # 짝수
        if matrix[0][i] == i+1:
            continue
        result += 1
    
    print(result)