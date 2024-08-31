"""
# 문제 링크: https://www.acmicpc.net/problem/2839
# 문제 설명
- 사탕 가게에 설탕을 배달하고자 한다. 설탕은 3kg / 5kg 주머니로 되어 있다.
- 배달하고자 하는 설탕 N kg을 위 두개를 조합해 배달해야 한다.
- N이 주어졌을 때, 들고가기 위한 최소한의 주머니 수를 세시오

# 접근법
- DP를 공부해야겠다 싶어 진행 중입니다.
- N개의 무게는 다음과 같이 쪼갤 수 있습니다.
    - (N - 3)kg + 3kg
    - (N - 5)kg + 5kg
    - 여기서, (N - 3)kg 과 (N - 5)kg을 몇 개의 주머니로 가져갈 수 있는지 안다면, 둘 중 최소 값을 선택하면 됩니다.
"""
N = int(input())

DP = [0 for n_iter in range(5001)]
DP[1] = float('inf')
DP[2] = float('inf')
DP[3] = 1
DP[4] = float('inf')
DP[5] = 1

for i in range(5, N+1):
    case1 = DP[i - 3] + DP[3]
    case2 = DP[i - 5] + DP[5]

    DP[i] = min(case1, case2)

answer = DP[N] if DP[N] != float('inf') else -1
print(answer)