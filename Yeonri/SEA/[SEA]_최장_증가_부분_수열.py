T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    lst = list(map(int, input().split()))
    result = [1] * N
    
    # 수열 계산
    for i in range(1, N):
        for j in range(i):
            if lst[i] > lst[j]: # 만약 i가 클 때,
                result[i] = max(result[i], result[j] + 1) # max를 이용해서 더 큰수를 저장


    max_length = max(result)

    print(f"#{test_case} {max_length}")