T = int(input())

for test_case in range(1,T+1):
    # 주차장 개수, 차량 개수
    N,M = map(int,input().split())
    R = [int(input()) for _ in range(N)]
    W = [int(input()) for _ in range(M)]
    total = 0
    wait = []
    park = [0] * N # 주차장 개수 만큼 생성 후 0으로 만든다.
    # 차량의 입출력
    # 차량이 들어왔다. > 주차장 자리가 있을 때 > 주차를 시킨 후, 가격 계산
    #                                    > 주차 자리가 없을 때, 대기
    # 차량이 나갔을 때, > 해당 차량이 주차되어 있는 주차자리를 뺀다.
    # > wait에 차량이 존재할 때, wait에서 꺼낸 후 제거 pop > 가격 계산
    # 주차장 리스트를 만든다.
    i = 0

    while i < 2*M:
        car = int(input())

        if car > 0:
            if 0 in park:
                # 가장 가까운 곳
                p_idx = park.index(0)
                park[p_idx] = car
                total += R[p_idx] * W[car - 1]

            elif 0 not in park:
                wait.append(car)

        if car < 0:
            car = abs(car)
            p_idx = park.index(car)
            park[p_idx] = 0

            # 대기 차량이 존재할 때,
            if len(wait) > 0:
                car = wait.pop(0)
                park[p_idx] = car
                total += R[p_idx] * W[car-1]

        i += 1

    print(f"#{test_case} {total}")