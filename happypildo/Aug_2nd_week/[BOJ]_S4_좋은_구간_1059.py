"""
# 문제 설명
- 어떤 집합 S가 주어질 때,
- 여기서 양의 정수 A와 B에 대해 A < B를 만족하고, A <= x <= B를 만족하는 x가 집합 S에 없다면 좋은 구간이라 한다.
- 집합 S와 x가 주어질 때, 좋은 구간의 수를 출력하시오.

# 접근 방법
- x가 주어졌을 때, 이를 포함하고 집합 S 내의 원소가 포함되면 안 되기에, x보다 (직전에) 작은 값(left)과 (직후에) 큰 값(right)을 우선적으로 찾음 (sorting 이후)
- 이 때, 만들 수 있는 좋은 구간의 수는
    - left + 1 ~ x - 1 의 수와 x를 범위로 지정
    - x +1 ~ right - 1 의 수와 x를 범위로 지정
    - left + 1 ~ x - 1 의 수와 x +1 ~ right - 1 의 수로 범위를 지정
- 이 경우의 수를 세어서 출력
"""
L = int(input())
S = sorted(list(map(int, input().split())))
S = [0] + S
target = int(input())

target_idx = -1
for i in range(L):
    if S[i] < target < S[i+1]:
        target_idx = i

if target_idx == -1:
    print(0)
else:
    left = target - (S[target_idx] + 1)
    right = S[target_idx + 1] - 1 - target

    answer = left + right + left * right

    print(answer)