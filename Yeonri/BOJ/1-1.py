N = int(input())
func1 = 0

for i in range(1, N+1): # N + 1
    if i % 3 == 0 or i % 5 == 0: # 검사 횟수 1 + 1
        func1 += i # 값 더하기 1

print(func1) # 프린트 1

# 1 + 1 + N * (1+1+1) + 1
# 그러므로 N