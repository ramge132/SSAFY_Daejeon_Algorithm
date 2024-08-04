import sys
from collections import deque
sys.stdin = open('차량정비소.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    A_time = list(map(int, input().split()))
    B_time = list(map(int, input().split()))

    K_queue = deque(list(map(int, input().split())))
    wait_queue_window = deque()
    wait_queue_repair = deque()
    A_lst = [0] * N
    B_lst = [0] * M

    time = 0 # 현재 시간
    total = 0 # 결과 저장
    people_number = 1
    result = []

    while len(result) < K or any(isinstance(a, list) for a in A_lst) or any(isinstance(b, list) for b in B_lst):

        # 고객 도착 처리
        # K_queue를 이용해서 while문을 통해 접근을 한다.
        # 위에서 창구로 바로 이동하도록 만들어서 중복된 내용을 처리하게 되었다.
        # 창구 접수에서 대기 인원을 처리하도록 통합한다.
        while K_queue and K_queue[0] == time:
            K_queue.popleft()
            wait_queue_window.append([people_number, 0]) # 사람 번호, 시간
            people_number += 1

        # 접수 창구 처리
        # 접수가 완료 되었을 때, 차량 정비소 B_lst의 자리가 꽉 찼는지 확인을 한다.
        # 이후 차량 정비소에 바로 넣던지, 대기열에 놓을건지 생각을 한다.
        # 해당 로직을 바로 대기 큐에 전달을 하여, 정비소에서 처리를 하도록 변경하였다.

        for idx in range(N):
            if isinstance(A_lst[idx], list):
                person_num, A_cnt_time = A_lst[idx]
                if A_cnt_time < A_time[idx] - 1:
                    A_lst[idx][1] += 1
                else:
                    wait_queue_repair.append([person_num, idx + 1, 0])
                    A_lst[idx] = 0

            if A_lst[idx] == 0 and wait_queue_window:
                A_lst[idx] = wait_queue_window.popleft()

        # 정비 창구 처리
        for idx in range(M):
            if isinstance(B_lst[idx], list):
                person_num, A_idx, B_cnt_time = B_lst[idx]
                if B_cnt_time < B_time[idx] - 1:
                    B_lst[idx][2] += 1

                else:
                    result.append([person_num, A_idx, idx + 1])
                    B_lst[idx] = 0
                    # 비어있는 정비소 확인을 여기서 처리하지 말고 else문이 끝난 후 처리하도록 만들었다.

            if B_lst[idx] == 0 and wait_queue_repair:
                B_lst[idx] = wait_queue_repair.popleft()

        time += 1

    total = sum(p_num for p_num, A_num, B_num in result if A_num == A and B_num == B)

    if total == 0: total = -1
    print(f'#{test_case} {total}')

'''import sys
from collections import deque
sys.stdin = open('차량정비소.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    A_time = list(map(int, input().split()))
    B_time = list(map(int, input().split()))

    K_queue = deque(list(map(int, input().split())))
    wait_queue_window = deque()
    wait_queue_repair = deque()
    A_lst = [0] * N
    B_lst = [0] * M

    time = 0 # 현재 시간
    total = 0 # 결과 저장
    people_number = 1
    result = []

    while len(result) < K: # result의 수에 따른 종료 조건

        # 큐에 존재하는 모든 원하는 값의 인덱스를 추출하고 싶다.
        # enumerate를 이용해서 반복적으로 전부 추출한다.
        # 하나씩 추출한다.
        ''''''if time in K_queue:
            for idx in range(len(K_queue)): #
                if K_queue[idx] != time: continue
                if K_queue[idx] == time:
                    K_queue[idx] = -1
                    if 0 not in A_lst: # 자리가 꽉 찼을 때,
                        wait_queue_window.append([idx+1, 0]) # 사람 번호

                    else: # 자리가 존재할 때,
                        for i, val in enumerate(A_lst):
                            if val == 0:
                                A_lst[i] = [idx + 1, 0] # A_lst[i] = [idx + 1, 0] # 0값을 가지는 제일 빠른 창구 번호에 고객 번호, 들어간 시간 카운트
                                break''''''

        # K_queue를 이용해서 while문을 통해 접근을 한다.
        # 위에서 창구로 바로 이동하도록 만들어서 중복된 내용을 처리하게 되었다.
        # 창구 접수에서 대기 인원을 처리하도록 통합한다.

        while K_queue and K_queue[0] == time:
                K_queue.popleft()
                wait_queue_window.append([people_number, 0]) # 사람 번호, 시간
                people_number += 1

        for idx in range(N): # 접수 시간 확인 후, 다음 단계로 이동
            if isinstance(A_lst[idx], list): # 리스트 형태일 경우에만 처리
                person_num, A_cnt_time = A_lst[idx]

                if A_cnt_time < A_time[idx]: # 값이 같지 않을 때,
                    A_lst[idx][1] += 1# 접근 후, 하나 올려준다.

                ###
                # 접수가 완료 되었을 때, 차량 정비소 B_lst의 자리가 꽉 찼는지 확인을 한다.
                # 이후 차량 정비소에 바로 넣던지, 대기열에 놓을건지 생각을 한다.
                # 해당 로직을 바로 대기 큐에 전달을 하여, 정비소에서 처리를 하도록 변경하였다.

                else: # 접수가 완료 되었을 때,
                    if 0 not in B_lst: # 자리가 꽉 찼을 때,
                        wait_queue_repair.append([person_num, idx + 1, 0]) # 대기열에 고객 번호, 시간 ,창구 번호

                    else: # 수리고에 자리가 존재할 때, 수리고로 이동하고 0으로 초기화
                        for i in range(M):
                            if B_lst[i] == 0:
                                B_lst[i] = [person_num, idx + 1, 0]
                                break
                    A_lst[idx] = 0

            if A_lst[idx] == 0 and wait_queue_window:  # 대기 고객이 존재할 때,
                A_lst[idx] = wait_queue_window.popleft()  # 대기 고객을 꺼내서 저장


        for idx in range(M):
            if isinstance(B_lst[idx], list): # 값이 들어있을 때,
                person_num, A_idx, B_cnt_time = B_lst[idx]

                if B_cnt_time < B_time[idx]: # 수리 중
                    B_lst[idx][2] += 1  # 접근 후, 하나 올려준다.
                else: # 수리 끝
                    result.append([person_num, A_idx, idx + 1])
                    if wait_queue_repair: # 대기 고객이 존재할 때, ##### 여기서 처리하지 말고 else문이 끝난 후 처리하도록 만들었다.
                        B_lst[idx] = wait_queue_repair.popleft() # 대기 고객을 꺼내서 저장
                    else:
                        B_lst[idx] = 0
            # print(B_lst)

        time += 1 # 시간을 하나 올려준다.

    # print(B_lst)

    total = sum(p_num for p_num, A_num, B_num in result if A_num == A and B_num == B)

    if total == 0: total = -1
    # print(result)
    print(f'#{test_case} {total}')
'''
