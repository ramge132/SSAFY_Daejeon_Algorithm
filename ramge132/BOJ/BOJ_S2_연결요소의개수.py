# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(10000)

# DFS를 이용한 연결 요소 탐색 함수
def dfs(node, graph, visited):
    visited[node] = True
    # 현재 정점과 연결된 모든 정점을 탐색
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited)

N, M = map(int, input().split())  # N: 정점의 개수, M: 간선의 개수
graph = [[] for _ in range(N + 1)]  # 1번 정점부터 N번 정점까지 사용하므로 N+1 크기로 생성
visited = [False] * (N + 1)  # 방문 여부를 기록하는 리스트

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 연결 요소 개수 카운팅
connected_components = 0

# 모든 정점을 순회하며 방문하지 않은 정점에서 DFS 실행
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i, graph, visited)
        connected_components += 1

print(connected_components)
