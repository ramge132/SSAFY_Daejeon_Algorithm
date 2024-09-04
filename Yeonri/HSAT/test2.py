import sys
input = sys.stdin.readline

from collections import deque
def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur_node = queue.popleft()
        
        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_re = [[] for _ in range(n+1)]

for _ in range(m):
    s, t = map(int, input().split())
    graph[s].append(t)
    graph_re[t].append(s)

home, company = map(int, input().split())

from_home = [False for _ in range(n+1)]
from_home[company] = True
bfs(home, graph, from_home)

from_company = [False for _ in range(n+1)]
from_company[home] = True
bfs(company, graph, from_company)

to_home = [False for _ in range(n+1)]
bfs(home, graph_re, to_home)

to_company = [False for _ in range(n+1)]
bfs(company, graph_re, to_company)

cnt = 0
for i in range(1, n+1):
    if i == home or i == company:
        continue
    if from_home[i] and from_company[i] and to_home[i] and to_company[i]:
        cnt += 1

print(cnt)