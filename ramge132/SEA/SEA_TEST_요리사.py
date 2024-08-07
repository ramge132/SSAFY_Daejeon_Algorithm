# 문제: 요리사
# 알고리즘 분류: 백트래킹
# 시간 복잡도: O((N/2)^2 * 2^(N/2))
# N개의 재료 중 절반을 선택하는 모든 경우를 탐색하고 각 경우에 대해 맛 차이를 계산

# itertools의 combinations를 이용해 모든 조합을 구할 수 있음
from itertools import combinations

# 주어진 식재료들에 대한 시너지를 계산하는 함수
def calculate_synergy(ingredients, synergy_matrix):
    total_synergy = 0
    # 선택된 식재료들 쌍의 시너지를 모두 합산
    for i in range(len(ingredients)):
        for j in range(i + 1, len(ingredients)):
            total_synergy += synergy_matrix[ingredients[i]][ingredients[j]] + synergy_matrix[ingredients[j]][ingredients[i]]
    return total_synergy

# 각 테스트 케이스를 해결하는 함수
def solve(test_cases):
    results = []
    for t in range(len(test_cases)):
        N = test_cases[t]['N']  # 현재 테스트 케이스의 식재료 수
        S = test_cases[t]['S']  # 현재 테스트 케이스의 시너지 행렬
        
        min_diff = float('inf')  # 맛의 차이의 최소값을 무한대로 초기화
        ingredients = set(range(N))  # 0부터 N-1까지의 식재료 인덱스 집합
        
        # 모든 가능한 식재료 조합을 탐색 (N개의 식재료 중 N/2개를 선택)
        for comb in combinations(range(N), N//2):
            A = set(comb)  # A음식에 사용될 식재료들
            B = ingredients - A  # B음식에 사용될 나머지 식재료들
            
            # A음식과 B음식의 시너지 합 계산
            A_synergy = calculate_synergy(list(A), S)
            B_synergy = calculate_synergy(list(B), S)
            
            # A음식과 B음식의 맛 차이 계산
            diff = abs(A_synergy - B_synergy)
            # 최소 맛 차이 업데이트
            if diff < min_diff:
                min_diff = diff
        
        # 결과 저장
        results.append(f"#{t + 1} {min_diff}")
    return results


T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())  # 현재 테스트 케이스의 식재료 수
    S = []
    for _ in range(N):
        # 시너지 행렬 입력
        S.append(list(map(int, input().split())))
    # 테스트 케이스 저장
    test_cases.append({'N': N, 'S': S})

results = solve(test_cases)
for result in results:
    print(result)

