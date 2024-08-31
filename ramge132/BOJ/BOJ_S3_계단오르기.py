# https://www.acmicpc.net/problem/1149

def min_paint_cost(n, costs):
    # 비용 테이블 초기화
    min_cost = [[0] * 3 for _ in range(n)]
    
    # 첫 번째 집 초기화
    min_cost[0][0] = costs[0][0]
    min_cost[0][1] = costs[0][1]
    min_cost[0][2] = costs[0][2]
    
    # 비용 테이블 채우기
    for i in range(1, n):
        min_cost[i][0] = min(min_cost[i-1][1], min_cost[i-1][2]) + costs[i][0]
        min_cost[i][1] = min(min_cost[i-1][0], min_cost[i-1][2]) + costs[i][1]
        min_cost[i][2] = min(min_cost[i-1][0], min_cost[i-1][1]) + costs[i][2]
    
    # 마지막 집의 최소 비용
    return min(min_cost[n-1][0], min_cost[n-1][1], min_cost[n-1][2])

n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

print(min_paint_cost(n, costs))
