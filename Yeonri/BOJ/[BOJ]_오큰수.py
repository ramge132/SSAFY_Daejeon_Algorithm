N = int(input())

lst = list(map(int, input().split()))

stack = []
result = [-1] * N

for i in range(N):
    while stack and lst[stack[-1]] < lst[i]: # 스택에 저장된 마지막 값이 현재 선택된 리스트보다 작을 때,
        result[stack.pop()] = lst[i] # result의 stack에서 추출한 값에 lst 값을 저장한다.
    stack.append(i) # 스택에 인덱스를 추가한다.

print(*result)

# N = int(input())

# lst = []
# result = []
# max_num = 0

# lst = list(map(int, input().split()))

# for i in range(N-1, -1, -1): # 마지막 부터 탐색

#     if len(result) == 0:
#         result.append(-1) # 제일 마지막에 존재하는 수일 때, -1을 추가
#         max_num = lst[i]

#     else:
#         a = lst.pop() # a를 뺀다.
#         if max_num < a:
#             max_num = a

#         if a > lst[-1]: # a와 제일 마지막 수를 비교한다.
#             result.append(a)

#         elif max_num > lst[-1]:
#             result.append(max_num)

#         else:
#             result.append(-1)
#         # print(a, max_num)

# for i in result[::-1]:
#     print(i, end = ' ')


# max를 설정해서 값들을 비교한다.
# 만약 max가 갱신되면 lst에 저장된 값들 중 제일 큰 것이기 때문에
# -> lst에 존재하는 값들을 전부 없애고, max 값을 append한다.
# 입력값이 max보다는 작지만 lst[-1] 보다는 크면 lst[-1]을 pop, 입력값 append

# max = 0
# number_lst = list(map(int, input().split()))
# lst = []
# result = []

# for num in number_lst:
#     if max < num: # num이 max보다 클 때, 제일 큰 값이므로
#         max = num 
#         if len(lst) > 0: # lst에 저장된 값이 존재할 때,

#             # append를 사용하면 길이가 2 이상일 때, 2차원 배열이 생성된다.
#             # extend를 사용하여 요소를 추가한다.
            
#             result.extend([max] * len(lst)) # 리스트에 저장된 수 만큼 결과에 저장
#             lst = [] # 리스트 초기화
#             lst.append(max) # 리스트에 값 추가
#         else: # 리스트에 값이 없으면 저장
#             lst.append(max)

#     elif lst[-1] < num: # max보다 num이 작지만 맨 마지막에 들어온 수 보다 클 때,
#             lst.pop()
#             lst.append(num)
#             result.append(num)
#     else:
#          lst.append(num)

# if len(lst)  == 1: # 맨 마지막 수는 비교할 대상이 없기 때문에 -1 설정
#     result.append(-1)

# for i in result:
#      print(i, end= ' ')

# 입력을 받으면서 탐색을 해보자.
# 맨 먼저 들어온 수와 나중에 들어온 수를 비교하면서
# 큰값이 존재하면 뺀다.
# 그런데 큰값이 끝까지 존재하지 않으면?
# -1을 출력을 어떻게 하는가
# 밑의 방법과 똑같아짐

# 시간 초과
# def lastchk(lst):
#     if len(lst) == 1:
#         lst.pop(0)
#         print(-1)
#         return True

# while lst:
#     for i in range(1, len(lst)):

#         if lst[0] < lst[i]:
#             print(lst[i])
#             lst.pop(0)

#             if lastchk(lst):
#                 break

#         if lst[0] >= lst[len(lst) - 1]:
#             lst.pop(0)
#             print(-1)

#             if lastchk(lst):
#                 break