# Make DP table
DP = [0 for _ in range(31)]
DP[:4] = [0, 1, 3, 6]
for n_iter in range(4, 31):
    DP[n_iter] = DP[n_iter - 1] + DP[n_iter - 2] * 2 + DP[n_iter - 3]

T = int(input())
for t_iter in range(1, T+1):
    print(f"#{t_iter} {DP[int(input())]}")