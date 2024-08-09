# 시작 21:15 시간복잡도 줄이기 실패
import sys
sys.stdin = open('../../input.txt')

# b를 1씩 증가시키면서 확인
T = int(input())
result = ''
for test_case in range(1, T + 1):
    n = int(input())
    b = 0
    while True:
        b += 1
        c = n*b
        #  N**(1/2)는 항상 Float형 반환
        if c**(1/2) == int(c**(1/2)):
            break

    result += f'#{test_case} {b}\n'

print(result)



########################################
# 소인수 분해 방법 소인수분해해서 각 소인수가 짝수가 되면 제곱완성 하지만 이것또한 실패
# def smallest_b(n):
#     b = 1
#     i = 2

#     while i * i <= n:
#         cnt = 0
#         while n % i == 0:
#             n //= i
#             cnt += 1
        
#         # 홀수인 경우 `b`에 해당 소인수를 추가
#         if cnt % 2 == 1:
#             b *= i

#         i += 1
    
#     # 남아있는 소수가 제곱수가 아닌 경우 처리
#     if n > 1:
#         b *= n

#     return b

# result = ''

# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#     b = smallest_b(n)
#     result += f'#{test_case} {b}'