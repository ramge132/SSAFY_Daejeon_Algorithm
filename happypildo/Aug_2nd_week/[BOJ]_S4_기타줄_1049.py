"""
# 문제 설명
- 기타 줄은 6개인데, 여러 개의 기타에서 몇 개(N개)가 끊어져 줄을 갈아야 한다.
- 기타 줄은 M개의 브랜드에서 6개 묶음줄과 낱개 줄을 판매한다.
- 최소 N개의 줄을 구비하고자 할 때, 최소 금액은 얼마인가?
- 입력 및 출력 예시
```python
4 2     # N, M
12 3    # [브랜드 1] 6개 묶음 가격, 낱개 가격
15 4    # [브랜드 2] 6개 묶음 가격, 낱개 가격
```

# 접근 방식
- DP로 접근을 하고자 했고, 이전에 greedy를 공부할 때 **배수가 아니면 Greedy로 풀 수 있다**라는 점이 생각 나 다음과 같이 접근했습니다.
1. 1-6개 줄까지는 하나씩 비교해 가며 최소 금액을 찾는다.
2. 7개 줄부터는, 6개 줄을 살 때와 1개 줄을 살 때 금액을 합친다. (15개라면, 12개 살 때와 3개 살 때 금액의 합)
"""
NUM_OF_STRINGS = 6

N, M = list(map(int, input().split()))

# 브랜드의 모든 금액을 알 필요 없다. 단순히 묶음 줄 가격이 제일 싼 것과 낱개 줄 가격이 제일 싼 것을 고르면 된다.
price_6 = float('inf')          
price_1 = float('inf')

for m_iter in range(M):
    temp_6, temp_1 = list(map(int, input().split()))

    if price_6 > temp_6:
        price_6 = temp_6
    if price_1 > temp_1:
        price_1 = temp_1

DP = [0 for _ in range(N+6)]
# N = 6일 때까지는 하나씩 비교해 가며 결정한다. 낱개로 여러 개 사는 것이 저렴한지 vs. 묶음으로 사버리는게 싼 것인지
for target_count in range(1, 7):
    DP[target_count - 1] = min(price_1 * target_count, price_6)

# 이후부터는, target_count = a + b 형식으로 계산하여 DP/Greedy 기법을 쓴다.
for target_count in range(7, N+1):
    a = NUM_OF_STRINGS * (target_count // NUM_OF_STRINGS)
    b = target_count % NUM_OF_STRINGS

    # 인덱싱을 위해, target_count가 6의 배수일 경우 예외 처리
    if b == 0: a, b = a - 6, 6

    DP[target_count - 1] = DP[a - 1] + DP[b - 1]

print(DP[N - 1])

