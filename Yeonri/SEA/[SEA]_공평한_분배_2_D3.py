T = int(input())

for test_case in range(0,T):
    # 나눠 준 주머니 가운데 사탕의 개수가 가장 많은 것과 가장 적은 것의 사탕 개수 차이 최소
    N,K = map(int, input().split())
    A = list(map(int,input().split()))
    
    min_count = float('inf')
    A.sort()

    B = []
    # 가장 차이가 적은 주머니 선택
    for i in range(N - K + 1):
        result = A[i+K-1] - A[i]
        if min_count > result:
            min_count = result

    print(f'#{test_case+ 1} {min_count}')
