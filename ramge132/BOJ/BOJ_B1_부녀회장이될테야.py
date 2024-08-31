# https://www.acmicpc.net/problem/2775

def calculate(k, n):
    # 15x15 배열로 초기화 (0층부터 14층까지, 1호부터 14호까지)
    residents = [[0] * (n + 1) for _ in range(k + 1)]
    
    # 0층 초기화
    for i in range(1, n + 1):
        residents[0][i] = i
    
    # DP 계산
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            residents[i][j] = residents[i][j-1] + residents[i-1][j]
    
    return residents[k][n]

T = int(input())
results = []
for _ in range(T):
    k = int(input())
    n = int(input())
    results.append(calculate(k, n))

for result in results:
    print(result)
