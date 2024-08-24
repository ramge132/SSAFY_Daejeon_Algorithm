N = int(input())
dp = [0] * (N + 1)

# 0 0 0 0 0 0 0 0 0
# 0 0 1 1 2 ...

for i in range(2, N + 1):
    
    dp[i] = dp[i - 1] + 1 # 이전 연산 횟수 + 1
    
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1) # 2를 나눈 수에 저장된 연산 횟수 + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1) # 3을 나눈 수에 저장된 연산 횟수 + 1

print(dp[N])

# 그리디 알고리즘으로 해결할 수 없음.
# dfs 및 조합을 이용하면 시간 초과 오류가 생길 것으로 예상
# N = int(input())
# cnt = 0

# # while N != 1:
# #     if N % 3 == 0:
# #         N = int(N / 3)
# #         cnt += 1
# #     if N % 2 == 0:
# #         N = int(N / 2)
# #         cnt += 1
# #     else:
# #         N -= 1
# #         cnt += 1

# while N != 1:
#     if N % 3 != 0:
#         while N % 3 != 0:
#             N -= 1
#             cnt += 1
#             if N == 1:
#                 break
#         continue

#     if N % 3 == 0:
#         N = int(N/3)
#         cnt += 1
#         continue
    
#     if N % 2 == 0:
#         N = int(N/2)
#         cnt += 1
#         continue

# print(cnt)