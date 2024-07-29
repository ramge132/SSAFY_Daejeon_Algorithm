T = int(input())

for test_case in range(1, T + 1):
    S = input().strip()
    E = input().strip()
    
    # S와 E의 길이가 같아질 때 까지
    # E의 문자를 제거해서 S와 같아질 수 있는지 확인한다.

    # 1. 제일 뒤에 X 붙이기
    # 2. 뒤집은 후 Y 붙이기

    while len(E) > len(S):
        if E[-1] == 'X':
            E = E[:-1]

        elif E[-1] == 'Y':
            E = E[:-1]
            E = E[::-1]

    if E == S:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')