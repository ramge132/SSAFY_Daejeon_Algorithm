# math의 comb 사용
# itertools보다 매우 빠름

import math

T = int(input())

for test_case in range(T):
    
    N, M = map(int, input().split())
    print(math.comb(M, N))

# itertools 사용
# from itertools import combinations

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     count = len(list(combinations(range(M), N)))

#     print(f'{count}')


# dfs 시간 초과..

# def dfs(index, current):
#     global count
    
#     # 다리를 전부 놓았다면 증가
#     if index == N:
#         count += 1
#         return
    
#     for i in range(current, M):
#         if not lst or lst[-1] < i: # 만약 오른쪽 다리가 선택된 i 보다 작을 때, 다리를 건설할 수 있음
#             lst.append(i)
#             dfs(index + 1, i + 1) # 다음 인덱스 확인
#             lst.pop()

# T = int(input())

# for test_case in range(1, T + 1):

#     N, M = map(int, input().split())
#     count = 0
#     lst = []
    
#     dfs(0, 0)

#     print(f'#{test_case} {count}')
