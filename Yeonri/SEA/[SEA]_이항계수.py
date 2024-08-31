import sys
sys.stdin = open('이항계수.txt', 'r')

T = int(input())

def chk():
    if A > B:
        return dp[-1][A]
    else:
        return dp[-1][B]
    
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())

    dp =[[0 for _ in range(N+1)] for _ in range(N + 1)]

    result = 0

    for i in range(N+1):
        for j in range(N+1):
            if i == j or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    result = chk()

    print(f'#{test_case} {result}')