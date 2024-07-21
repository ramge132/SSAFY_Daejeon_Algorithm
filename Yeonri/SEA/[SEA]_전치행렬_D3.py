'''
A[i,j]와 A[i][j]의 접근 차이?
주요 차이점은 a[i][j]먼저 뷰를 만든 a[i]다음 해당 뷰로 인덱싱한다는 것입니다. 반면에 a[i,j]직접 인덱싱하여 a더 빠르게 만듭니다.
'''
T = int(input())

for test_case in range(1, T + 1):
    # 행렬 전치해서 정렬하기
    
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]
	
    # 전치 후 배열에 존재하는 숫자들이 정렬된 배열과 같은지 확인?
    
    # 전치 시키기
    # 0부터 시작
    count = 0

    # 리스트를 평탄화해서 정렬된 리스트 생성
    sorted_lst = sorted(sum(lst,[]))

    while True:
        chk_lst = sum(lst, [])

        if chk_lst == sorted_lst:
            break
        else:

            # 전치
            # (1,1) (1,2) (1,3)
            # (2,1) (2,2) (2,3)
            # (3,1) (3,2) (i,i)

            count += 1
            lst = [[lst[i][j] for j in range(N)] for i in range(N)]
            '''
            for i in range(N):
                for j in range(i+1, N):
                    lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
            '''

            # 21131. 행렬정렬 D3

    print(f'#{test_case} {count}')
