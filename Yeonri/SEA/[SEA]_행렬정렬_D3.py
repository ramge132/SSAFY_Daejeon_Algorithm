'''
정렬된 상태의 리스트를 미리 만들어둠 (1부터 N*N까지)
현재 행렬이 정렬된 상태인지 확인
정렬되지 않았다면, 전치할 부분 행렬의 크기를 찾음
>> 오른쪽 아래 대각선에서 정렬되지 않은 가장 큰 원소의 위치가 x
x*x 크기의 부분행렬을 전치
'''

T = int(input())

for test_case in range(1, T + 1):
    # 행렬 정렬하기
    
    N = int(input())

    lst = [list(map(int,input().split())) for _ in range(N)]
	
    count = 0

    # 전치 후 배열에 존재하는 숫자들이 정렬된 배열과 같은지 확인해야함
    # 리스트를 평탄화해서 정렬된 리스트 생성 >> 1차원 평탄화 중요
    sorted_lst = list(range(1, N*N + 1))

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
            
            # 전치할 부분 행렬의 크기 찾기
            x = N
            while x > 0:
                if lst[x-1][x-1] != x*x: # 행렬의 최대 크기를 찾는다. >> 원소를 변경할 위치로 이동시키기 위함
                    break
                x -= 1
            
            # x*x 크기의 부분행렬 전치
            for i in range(x):
                for j in range(i, x):
                    lst[i][j], lst[j][i] = lst[j][i], lst[i][j] # 서로의 위치를 변경

    print(f'#{test_case} {count}')


# '''
# A[i,j]와 A[i][j]의 접근 차이?
# 주요 차이점은 a[i][j]먼저 뷰를 만든 a[i]다음 해당 뷰로 인덱싱한다는 것입니다. 반면에 a[i,j]직접 인덱싱하여 a더 빠르게 만듭니다.
# '''
# T = int(input())

# for test_case in range(1, T + 1):
#     # 행렬 전치해서 정렬하기
    
#     N = int(input())

#     lst = [list(map(int,input().split())) for _ in range(N)]
	
#     # 전치 후 배열에 존재하는 숫자들이 정렬된 배열과 같은지 확인?
    
#     # 전치 시키기
#     # 0부터 시작
#     count = 0

#     # 리스트를 평탄화해서 정렬된 리스트 생성
#     sorted_lst = sorted(sum(lst,[]))

#     while True:
#         chk_lst = sum(lst, [])

#         if chk_lst == sorted_lst:
#             break
#         else:

#             # 전치
#             # (1,1) (1,2) (1,3)
#             # (2,1) (2,2) (2,3)
#             # (3,1) (3,2) (i,i)

#             count += 1
#             lst = [[lst[i][j] for j in range(N)] for i in range(N)]
#             '''
#             for i in range(N):
#                 for j in range(i+1, N):
#                     lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
#             '''

#             # 21131. 행렬정렬 D3

#     print(f'#{test_case} {count}')
