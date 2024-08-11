# SWEA D3 햄버거 다이어트와 상당히 유사한 문제

def dfs(idx, cost, protein, fat, carb, vit):
    global min_cost, result, select
    
    # 최소 영양 기준을 만족하는 경우
    if protein >= mp and fat >= mf and carb >= ms and vit >= mv:
        if cost < min_cost or (cost == min_cost and select < result):
            min_cost = cost
            result = select[:]
        return
    
    # 모든 재료 확인 >> 종료
    if idx == N:
        return
    
    # 현재 식재료를 선택하지 않는 경우
    dfs(idx + 1, cost, protein, fat, carb, vit)
    
    # 현재 식재료를 선택하는 경우 번호 인덱스를 저장한다.
    select.append(idx + 1)

    dfs(idx + 1, cost + costs[idx], protein + proteins[idx], fat + fats[idx], carb + carbs[idx], vit + vitamins[idx])
    
    # 선택된 것을 취소해야 한다.
    # 취소하지 않으면 탐색을 하고 돌아왔을 때, 선택 결과가 그대로
    # 리스트에 저장되어 있기 때문이다.
    select.pop()

N = int(input())

mp, mf, ms, mv = map(int, input().split())

proteins = []
fats = []
carbs = []
vitamins = []
costs = []

for _ in range(N):
    p, f, s, v, c = map(int, input().split())
    proteins.append(p)
    fats.append(f)
    carbs.append(s)
    vitamins.append(v)
    costs.append(c)

min_cost = float('inf')
result = []
select = []

dfs(0, 0, 0, 0, 0, 0)


print(min_cost)
print(' '.join(map(str, sorted(result))))
