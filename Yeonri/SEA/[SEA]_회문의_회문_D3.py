T = int(input())

for test_case in range(1, T + 1):
    # 1차 chk (N-1)/2 가 회문 내부 내용 K
    # 2차 chk (K-1)/2 가 회문
    
    S = input()
    N = len(S)
    K = (N - 1) // 2

    flag = False
    if S == S[::-1]:

        First_S2 = S[:K]
        # Last_S2 = S[-K:]

        # 왼쪽 문자 검사
            # 오른쪽 문자 검사
        # 회문의 회문 >> 왼쪽이 같으면 오른쪽도 같다.

        if First_S2 == First_S2[::-1]:
            # print(First_S2)
            # print(Last_S2)
            flag = True
            
            '''if Last_S2 == Last_S2[::-1]:
                print(Last_S2)
                flag = True'''
        
    else:
        flag = False
    
    if flag == True:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')