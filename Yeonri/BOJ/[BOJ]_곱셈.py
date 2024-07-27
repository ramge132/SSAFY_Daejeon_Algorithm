# A를 B번 곱한수를 C로 나눈 나머지

# A**n * A**n = A**2n
# A**B = A**B/2 * A**B/2

def mult(a, b, c):
    if b == 0:
        return 1  # A**0은 항상 1
    if b == 1:
        return a % c  # A**1은 A를 c로 나눈 나머지
    
    half = mult(a, b // 2, c)
    half = (half * half) % c
    
    if b % 2 == 0:
        return half  # b가 짝수인 경우
    else:
        return (half * a) % c  # b가 홀수인 경우

A, B, C = map(int, input().split())
print(mult(A, B, C))
