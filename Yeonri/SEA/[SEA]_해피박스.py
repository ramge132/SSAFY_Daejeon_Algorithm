import sys
sys.stdin = open('해피박스.txt', 'r')
from pprint import pprint
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    weight = []
    price = []
    total = 0
    for _ in range(M):
        w, p = map(int, input().split())
        weight.append(w)
        price.append(p)
    
    dp = [[0] * (N+1) for _ in range(M)]
    
    for i in range(0, M):
        for w in range(1, N + 1):
            if weight[i - 1] > w:
                dp[i][w] = dp[i-1][w] # 이전에 작성된 값 작성
            else:
                dp[i][w] = max(price[i-1]+ dp[i-1][w - weight[i-1]], dp[i-1][w])
                total = dp[i][w]
        # print(total)
    # for i in range(M):
    #     print(dp[i])
    print(f'#{test_case} {total}')