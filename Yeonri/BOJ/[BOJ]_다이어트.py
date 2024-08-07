def dfs(idx, cost, protein, fat, carb, vit):
    global min_cost, result, select
    
    # 최소 영양 기준을 만족하는 경우

    ## 입력된 기준보다 높거나 같아야 한다.
    ## 사전 순으로 가장 빠른 것을 출력해야 된다.

    if protein >= mp and fat >= mf and carb >= ms and vit >= mv:
        if cost < min_cost or (cost == min_cost and select < result):
            min_cost = cost
            result = select[:] # <<<<< 리스트의 값 자체를 복사.
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

# 조건을 만족하는 답이 없다면 -1을 출력하고, 둘째 줄에 아무것도 출력하지 않는다.
# 해당 조건을 추가하였다.

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(' '.join(map(str, sorted(result))))

# SWEA D3 햄버거 다이어트와 상당히 유사한 문제
# 변수의 개수와 종료 조건문이 추가되었다.
# result에 select를 저장하는데 select 값이 바뀌니까 같이 바뀌는 현상이 생김
# 리스트가 참조 변수이기 때문에 result에 select가 참조하는 메모리의 주소를 반환하였기 때문이다.
# 따라서 result에 select[:]를 하여 값 자체를 새로 부여했다.