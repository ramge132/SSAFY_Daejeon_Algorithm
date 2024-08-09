N = int(input())

dict= {3: 0, 5:0}
total = 0

# 3으로 먼저 빼 나가고, 5로 나누면 나머지가 0 일때 5의 개수를 저장하고 종료
# 만약 3보다 값이 작아지면 total = -1 , 종료

while True:
    if N == 0:
        total = sum(dict.values())
        break

    if N < 3:
        total -= 1
        break

    if N % 5 != 0:
        N -= 3
        dict[3] += 1
    else:
        dict[5] = N // 5
        N = 0

print(total)

    # 이 방법을 사용할 경우, 5를 먼저 계산하기 때문에 11과 같은 3으로 빼야 되는 값이면 결과 도출 불가능
    # if N >= 5:
    #     N = N - 5
    #     dict[5] += 1
    # elif N >= 3:
    #     N = N - 3
    #     dict[3] += 1
    # else:
    #     total = -1
    #     break
    
    
    # %를 사용할 경우 제일 큰 수를 먼저 이용하기 때문에 작은 값을 먼저 계산해야 하는 경우를 판단하지 못함
    
    # if N >= 5:
    #     dict[5] = N // 5
    #     N = N % 5
    # 
    # elif N >= 3:
    #     dict[3] = N // 3
    #     N = N % 3
    #     if N != 0:
    #         total = -1
    #         break
    # 
    # else:
    #     total = -1
    #     break