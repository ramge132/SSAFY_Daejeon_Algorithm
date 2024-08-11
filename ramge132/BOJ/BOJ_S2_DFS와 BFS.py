# https://www.acmicpc.net/problem/1260

from collections import deque


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    for next_node in graph[start]:
        if not visited[next_node]:
            dfs(graph, next_node, visited)


def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for next_node in graph[v]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 정점에 연결된 다른 정점들을 미리 정렬
for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
bfs(graph, v)
