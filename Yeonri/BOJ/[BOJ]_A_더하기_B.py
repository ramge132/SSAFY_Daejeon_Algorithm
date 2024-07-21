# 0 < A, B < 0
A, B = input().split()

# A와 B가 int 타입의 범위를 벗어났을 때,
# A 혹은 B가 소숫점을 가지고 있을 때, float


result = float(A) + float(B)

# # 문자열로 .0이 존재하는지 확인
# if '.0' in f'{result}':
#     result = int(result)

# result에 들어있는 값이 정수형태로 존재하는지 확인
if result.is_integer():
    result = int(result)

print(result)
