# https://www.acmicpc.net/problem/2839

# 1. 그리디 / 88ms
def sugar(N):
    for x in range(N // 5, -1, -1):  # 5킬로그램 봉지를 최대한 많이 사용
        remainder = N - 5 * x
        if remainder % 3 == 0:  # 나머지가 3으로 나누어 떨어지면
            return x + (remainder // 3)  # 총 봉지 수 (5킬로그램 봉지 수 + 3킬로그램 봉지 수)
    return -1  # 정확하게 N킬로그램을 만들 수 없는 경우

N = int(input())
print(sugar(N))


######################################################################################

# 2. DP / 88ms
def sugar_dp(N):
    # DP 테이블 초기화
    dp = [float('inf')] * (N + 1)
    dp[0] = 0  # 0kg은 봉지 필요 없음

    # DP 계산
    for i in range(3, N + 1):
        if i >= 3:
            dp[i] = min(dp[i], dp[i - 3] + 1)
        if i >= 5:
            dp[i] = min(dp[i], dp[i - 5] + 1)

    # 결과 반환
    return dp[N] if dp[N] != float('inf') else -1

N = int(input())
print(sugar_dp(N))
