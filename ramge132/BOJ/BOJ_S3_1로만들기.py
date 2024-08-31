# https://www.acmicpc.net/problem/1463

def count_ways(n):
    dp = [0] * (n + 1)
    
    # 초기값 설정
    dp[1] = 1
    if n >= 2:
        dp[2] = 2
    if n >= 3:
        dp[3] = 4
    
    # DP 테이블 채우기
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    results.append(count_ways(n))

for result in results:
    print(result)
