# 리스트에 넣고 in을 통한 탐색으로 문제 해결
# 뭐가 문제인지 모르곘음

N = int(input())
numbers = set(map(int, input().split()))

M = int(input())
compare_numbers = list(map(int, input().split()))

for num in compare_numbers:
    print(1 if num in numbers else 0)



# 리스트의 인덱스에 접근해서 빠르게 탐색하도록 하려고 함
# 런타임 오류 발생

# N = int(input())
# num = [False] * (N + 1)

# numbers = list(map(int, input().split()))

# for i in numbers:
#     num[i] = True

# M = int(input())

# compare_num = list(map(int, input().split()))

# for i in compare_num:
#     if 0 <= i <= N:
#         print(1 if num[i] else 0)
#     else:
#         print(0)


    # if i >= len(num):
    #     print(0)
    # else:
    #     print(1 if num[i] else 0 )
    #     # if num[i]:
    #     #     print(1)
    #     # else:
    #     #     print(0)