N = int(input())
arr = list(map(int, input().split()))
DP = [1 for _ in range(N)]

for i in range(len(arr)):
    for j in range(i, -1, -1):
        DP[i] = max(DP[i], DP[i - j] + 1 if arr[i - j] < arr[i] else 1)

print(max(DP))