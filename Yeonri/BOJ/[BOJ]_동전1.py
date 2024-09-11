N, K = map(int, input().split())

dp = [[0] * K for _ in range(N)]
coin = []

for _ in range(N):
    coin.append(int(input()))

coin.sort()

for i in range(K):
    
for i in range(1, N):
    for j in range(1, K):
        dp[i][j] = dp[i][j-1] + dp[i - 1][j - coin[i]]

print(dp)