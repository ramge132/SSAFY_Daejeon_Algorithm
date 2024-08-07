# https://www.acmicpc.net/problem/15686


# 1. 일반 버전 / 148 ms, 111496 KB
from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken_shops = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_shops.append((r, c))

# 치킨 거리를 계산하는 함수
def chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

# 모든 치킨집 조합 중에서 최적의 조합을 탐색
min_distance = float('inf')
for chickens in combinations(chicken_shops, M):
    min_distance = min(min_distance, chicken_distance(chickens))

print(min_distance)



###############################################


# 2. 백트래킹 버전 / 176 ms, 112552 KB
def chicken_distance(selected_chickens):
    total_distance = 0
    for hx, hy in houses:
        min_distance = float('inf')
        for cx, cy in selected_chickens:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        total_distance += min_distance
    return total_distance

def backtrack(start, selected_chickens):
    global min_distance
    if len(selected_chickens) == M:
        min_distance = min(min_distance, chicken_distance(selected_chickens))
        return
    
    for i in range(start, len(chicken_shops)):
        selected_chickens.append(chicken_shops[i])
        backtrack(i + 1, selected_chickens)
        selected_chickens.pop()

# 사용자로부터 N과 M을 입력받습니다.
N, M = map(int, input().split())

# N개의 수를 입력받습니다.
city = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 위치를 저장합니다.
houses = []
chicken_shops = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            houses.append((r, c))
        elif city[r][c] == 2:
            chicken_shops.append((r, c))

# 최솟값을 저장할 변수 초기화
min_distance = float('inf')

# 백트래킹 시작
backtrack(0, [])

# 결과 출력
print(min_distance)
