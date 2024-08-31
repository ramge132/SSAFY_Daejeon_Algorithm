# https://www.acmicpc.net/problem/1003

def count_fibonacci_zeros_ones(n):
    count_zeros = [0] * (n + 1)
    count_ones = [0] * (n + 1)
    
    # 초기값 설정
    count_zeros[0] = 1
    count_ones[0] = 0
    if n >= 1:
        count_zeros[1] = 0
        count_ones[1] = 1
    
    # count 배열 계산
    for i in range(2, n + 1):
        count_zeros[i] = count_zeros[i-1] + count_zeros[i-2]
        count_ones[i] = count_ones[i-1] + count_ones[i-2]
    
    return count_zeros[n], count_ones[n]

T = int(input())
results = []
for _ in range(T):
    n = int(input())
    results.append(count_fibonacci_zeros_ones(n))

for result in results:
    print(result[0], result[1])
