"""
# 문제 설명
- 길이 N의 A와 B 수열이 주어졌을 때, C = A[0] * B[N-1] + A[1] * B[N-2] ...를 계산한다.
- 이 떄, C를 최소값으로 만들기 위해 A 수열을 재배열할 수 있다.
- 그 때의 C 값을 구하시오.

# 접근 방법
- 작은 값과 큰 값이 곱해지는 것이 최적이므로 정렬해서 풀었습니다.
"""
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A, reverse=True)
B = sorted(B)

answer = 0
for a, b in zip(A, B):
    answer = answer + a * b

print(answer)