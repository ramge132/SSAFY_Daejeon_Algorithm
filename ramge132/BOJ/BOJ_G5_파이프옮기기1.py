# https://www.acmicpc.net/problem/17070

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# dp[r][c][d]: (r, c) 위치에 방향 d(0: 가로, 1: 세로, 2: 대각선)로 올 수 있는 방법의 수
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]

# 초기 상태
dp[0][1][0] = 1

# DP 수행
for r in range(N):
    for c in range(1, N):
        if grid[r][c] == 1:
            continue
        # 가로 방향
        if c > 0:
            dp[r][c][0] += dp[r][c-1][0] + dp[r][c-1][2]
        # 세로 방향
        if r > 0:
            dp[r][c][1] += dp[r-1][c][1] + dp[r-1][c][2]
        # 대각선 방향
        if r > 0 and c > 0 and grid[r-1][c] == 0 and grid[r][c-1] == 0:
            dp[r][c][2] += dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]

# 최종 결과 출력
print(dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2])