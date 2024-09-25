import heapq
# 백준 빠리삐쁠~~~~~~~~~~
N, M, X = map(int, input().split())
result = 0

def dijkstra(start_node, end_node):
    # 우선순위 큐
    queue = []
    # 최단거리 초기화
    # distances = [0 if idx == start_node-1 else float('inf') for idx in range(N)]
    distances = [float('inf') for _ in range(N)]
    distances[start_node - 1] = 0

    heapq.heappush(queue, (0, start_node))
    while queue:
        cost, current_node = heapq.heappop(queue)
        
        for connected, connected_cost in graph[current_node]:

            # 이미 초기화한 최단거리가 더 빠를 때 패스
            if distances[connected - 1] < connected_cost + cost:
                continue

            else:
                distances[connected - 1] = connected_cost + cost
                if connected != end_node:
                    heapq.heappush(queue, (distances[connected - 1], connected))

    return distances[end_node - 1]


graph = {}
for _ in range(M):
    # 시작점, 끝점, 가중치
    start, end, time = map(int, input().split())
    # 키가 있는 경우
    if graph.get(start):
        graph[start].add((end, time))
    # 키가 없는 경우
    else:
        graph[start] = {(end, time)}

for student in range(1, N+1):
    if student == X:
        continue

    cost = dijkstra(student, X)
    cost += dijkstra(X, student)
    
    if cost > result:
        result = cost

print(result)