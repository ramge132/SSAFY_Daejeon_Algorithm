import sys
sys.stdin = open('파도반수열.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = 0

    if N <= 2:
        result = 1
        print(f'#{test_case} {result}')
        continue
    
    dp = [0] * (N + 1)
    for i in range(3):
        dp[i] = 1
    
    for i in range(3, N + 1):
        dp[i] = dp[i - 3]+ dp[i - 2]
    
    result = dp[N - 1]

    print(f'#{test_case} {result}')

    # print(dp)