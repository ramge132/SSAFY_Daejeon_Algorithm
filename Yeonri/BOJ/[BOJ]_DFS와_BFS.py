from collections import deque

N, M, V = map(int, input().split())

graph = {}
visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1) 

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    
    if v in graph:
        for next_v in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
            if not visited_dfs[next_v]:
                dfs(next_v)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        if v in graph:
            for i in sorted(graph[v]):
                if not visited_bfs[i]:
                    queue.append(i)
                    visited_bfs[i] = True


for _ in range(M):
    s, e = map(int, input().split())
    if s not in graph:
        graph[s] = [e]
    else:
        graph[s].append(e)
    
    if e not in graph:
        graph[e] = [s]
    else:
        graph[e].append(s)
    

dfs(V)
print()

bfs(V)
print()