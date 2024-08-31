import sys
sys.stdin = open('보호필름.txt', 'r')


from itertools import combinations
import pprint

# def inspect():
#     for w in range(W):
#         # 시작 셀의 연속된 특성은 1부터
#         k_sum = 1

#         for j in range(D - 1):
#             if matrix[j][w] == matrix[j + 1][w]:
#                 k_sum += 1
#             else:
#                 k_sum = 1

#             if k_sum == K:
#                 break

#         # 위의 내부 for문을 끝까지 돈다 -> 성능 K에 도달 못함
#         else:
#             return False
    
#     return True

# # 약품 투입 횟수
# def dfs(depth):
#     # 종료 조건 -> 투입 횟수
#     if depth == len(selected_layers):
#         return inspect()
    
#     layer_depth = selected_layers[depth]
#     # 선택한 레이어를 바꾸면서 dfs 진행
#     # 바꾼 다음 무조건 되돌려야 한다.
#     tmp_arr = matrix[layer_depth]

#     # 목표 레이어 선택
#     matrix[layer_depth] = [0] * W
#     if dfs(depth+ 1):
#         return True
    
#     matrix[layer_depth] = [1] * W
#     if dfs(depth+ 1):
#         return True

#     matrix[layer_depth] = tmp_arr

#     pass


# T = int(input())

# for test_case in range(1, T + 1):
#     D, W, K = map(int, input().split())
#     matrix = [list(map(int, input().split())) for _ in range(D)]
#     min_inject_cnt = -1

#     # 약품 투입을 조합으로 해결할 것.
#     # 0번부터 D번까지

#     for inject_cnt in range(D + 1):
#         # 검사 로직
#         # 조합적으로 D 개 중에 1개를 선택
#         if inject_cnt == 0:
#             # 주어진 셀들 검사
#             if inspect():
#                 min_inject_cnt = 0
#                 break
        
#         # 두께 D 까지 있으면
#         for selected_layers in combinations(range(D), inject_cnt):
#             # dfs가 성공적이면 최소 투약 횟수를 최신화 후 종료
#             # 1. 재귀 호출을 종료할 파라미터 (selected layer의 개수)
#             # 투입 횟수
#             # 2. 누적 값 
#             if dfs(0):
#                 min_inject_cnt = inject_cnt
#                 break

#     print(f'#{test_case} {min_inject_cnt}')


T = int(input())

def medi(lst, sel_num, cnt):
    global result

    if cnt == K:
        result = min(result, cnt)
        return

    if result <= cnt:
        return    
            
    if chk(lst):
        result = min(result, cnt)
        return

    if sel_num == D:
        return

    # 약품 처리 A와 B 두가지 존재
    # 각 열을 선택해서 변경해야 됨

    # 선택하였을 때, 

    medi(lst, sel_num + 1, cnt) # 변경 하지 않음

    a_lst = lst[sel_num][:]
    medi(change(sel_num, lst, 0), sel_num + 1, cnt + 1) # 0으로 변경
    
    # lst[sel_num] = a_lst
    # b_lst = lst[sel_num][:]

    medi(change(sel_num, lst, 1), sel_num + 1, cnt + 1) # 1로 변경
    lst[sel_num] = a_lst
    # lst를 변경해서 사용하고 있으므로, 같이 사용하는 lst가 변경된다.    

def change(sel_num, lst, num):
    for j in range(W):
        lst[sel_num][j] = num
    return lst

# 틀린 코드
# def chk(lst):
#     # 만약 count == 1이 아니면 약품을 투입
#     for j in range(W):
#         count = 1
#         for i in range(D - 1):
#             if lst[i][j] == lst[i + 1][j]:
#                 count += 1

#                 if count == K:
#                     break

#             else:
#                 return False

#     return True

# 수정한 틀린 코드
# def chk(lst):
#     # 만약 count == 1이 아니면 약품을 투입
#     for j in range(W):
#         count = 1
#         for i in range(D - 1):
#             if lst[i][j] == lst[i + 1][j]:
#                 count += 1

#                 if count == K:
#                     break
            
#             else:
#                 count = 1 # 다른 숫자가 나왔을 때, count를 1로 설정하여 나머지 숫자들도 확인한다.
#         else: # for문이 break되지 않고 나왔을 때, else를 이용하여 실패를 알리는 return False를 한다.
#             return False
#     return True

def chk(lst):
    # 만약 count == 1이 아니면 약품을 투입
    for j in range(W):
        count = 1
        for i in range(D - 1):
            if lst[i][j] == lst[i + 1][j]:
                count += 1

                if count == K:
                    break
            
            else:
                count = 1 # 다른 숫자가 나왔을 때, count를 1로 설정하여 나머지 숫자들도 확인한다.
        
        if count < K:
            return False

    return True

# for - else 구문 사용
# def chk(lst):
#     # 만약 count == 1이 아니면 약품을 투입
#     for j in range(W):
#         count = 1
#         for i in range(D - 1):
#             if lst[i][j] == lst[i + 1][j]:
#                 count += 1

#             else:
#                 count = 1

#             if count == K: # 연속된 값이 존재할 때, TRUE일 때, break로 for문을 종료한다.
#                 break
#         else:
#             # for - else구문 -> 만약 위의 for문에서 조건을 만족하지 못하여 for문을 전부 돌고 나왔을 때, else를 이용해서 return False
#             return False

#     return True


for test_case in range(1, T+1):
    D, W, K = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(D)]

    # 약품을 사용해서 번호 변경
    # 위치 선택 -> 동일한 번호가 존재하는지 파악

    result = float('inf')
    medi(matrix, 0, 0)
    print(f'#{test_case} {result}')