"""
# 문제 링크: https://www.acmicpc.net/problem/1463
# 문제 설명:
- 정수 X에
    1. 3으로 나누어 떨어지면, 3으로 나눈다
    2. 2로 나누어 떨어지면, 2로 나눈다.
    3. 1을 뺀다.
    - 이 세 개의 연산을 할 수 있다.
- 최소한의 연산으로 1이라는 숫자를 만들고자 한다. 최소 연산 수를 구하시오.

# 문제 접근법:
- DP[X]를 정수 X를 1로 만들기 위한 연산 수 라고 할 때,
    - `DP[i // 3] + 1 if i % 3 == 0 else float('inf')`
    - `DP[i // 2] + 1 if i % 2 == 0 else float('inf')`
    - `DP[i - 1] + 1`
    - 로 구성할 수 있다.

# 왜 DP로 풀어야 할까? Greedy는 왜 안 되는가?
- 먼저, 하위 문제로 구성될 수 있기 때문에 DP가 적합하다.
- 다음으로, Greedy로 푼다면 `N=10`일 때 반례가 생긴다.
"""
DP = [float('inf') for i in range(10 ** 6 + 1)]
DP[0:4] = [0, 0, 1, 1]

N = int(input())
for i in range(4, N + 1):
    A = DP[i // 3] + 1 if i % 3 == 0 else float('inf')
    B = DP[i // 2] + 1 if i % 2 == 0 else float('inf')
    C = DP[i - 1] + 1

    DP[i] = min(A, B, C)

print(DP[N])