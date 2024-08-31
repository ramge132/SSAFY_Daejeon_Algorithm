# Make DP table
layer_cnt = [x for x in range(1, 72)]
DP = [1 for _ in range(sum(layer_cnt))]
DP[0] = 0
offset = layer_cnt[2]
for layer in layer_cnt[2:]:
    for i in range(layer):
        if i == 0 or i == layer - 1: continue
        else: DP[offset + i] = DP[offset + i - layer] + DP[offset + i - layer + 1]
    offset += layer

T = int(input())
for t_iter in range(1, T+1):
    n, a, b = list(map(int, input().split()))
    offset = sum(layer_cnt[:n + 1]) - 1 - a
    print(f"#{t_iter} {DP[offset]}")