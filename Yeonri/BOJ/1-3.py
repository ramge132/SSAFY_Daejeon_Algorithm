# 제곱수면 1 아니면 0

N = int(input())

result = 0

for i in range(N):
    if i*i == N:
        result = 1
        break

print(result)

# O(root N)
# 제곱 값을 구해서 N을 찾는 것 이기 때문에 루트 N이 된다.