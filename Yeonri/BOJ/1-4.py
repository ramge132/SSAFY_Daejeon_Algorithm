N = int(input())


result = 0

for i in range(N+1):
    if 2**i <= N:
        result = 2**i
    else:
        break

print(result)
# 2**i = N 으로 진행되었다.
# 따라서 O(logN)