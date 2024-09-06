'''
from collections import deque

# def dfs(start, end, route_set, depth=0):
#     print(depth)
#     if depth > n*n-1:
#         return
    
#     if start == end:
#         # 출근 길
#         if end == t:
#             can_arrive.add(tuple(route_set))
#         # 퇴근 길
#         elif end == s:
#             can_come.add(tuple(route_set))

#         return

#     for next_node in graph[start]:
#         temp_routes = route_set.copy()
#         temp_routes.add(next_node)

#         dfs(next_node, end, temp_routes, depth+1)


def bfs(queue, end, visited):
    global can_arrive
    global can_come

    while queue:
        node_no, route = queue.popleft()

        for next_node in graph[node_no]:
            if next_node in visited or next_node == end:
                continue

            if not graph[next_node]:
                continue

            visited.add(next_node)
            queue.append([next_node, route + [next_node]])

    
    if end == t:
        visited.discard(s)
        can_arrive |= visited
    
    elif end == s:
        visited.discard(t)
        can_come |= visited



n, m = map(int, input().split())
route_inputs = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

graph = {}

can_arrive = set()
can_come = set()

result_node = set()

for i in range(1, n+1):
    graph[i] = set()


for start, end in route_inputs:
    if graph.get(start):
        graph[start].add(end)
    else:
        graph[start] = set([end])


# bfs
bfs(deque([[s, [s]]]), t, {s})

bfs(deque([[t, [t]]]), s, {t})

print(len(can_come & can_arrive))
'''
'''
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
'''

from collections import deque

def bfs(queue, end_point, direction, visited):
    global work_can_come
    while queue:
        number = queue.popleft()

        if number == end_point:
            continue

        if end_point == t:
            if direction == 'front':
                for next_number in graph[number]['front']:
                    if next_number in visited or next_number == end_point:
                        continue
                    else:
                        visited.add(next_number)
                        home_can_go.add(next_number)
                        queue.append(next_number)
            else:
                for next_number in graph[number]['back']:
                    if next_number in visited or next_number == end_point:
                        continue
                    else:
                        visited.add(next_number)
                        work_can_come.add(next_number)
                        queue.append(next_number)
        
        else:
            if direction == 'front':
                for next_number in graph[number]['front']:
                    if next_number in visited or next_number == end_point:
                        continue
                    else:
                        visited.add(next_number)
                        work_can_go.add(next_number)
                        queue.append(next_number)
            else:
                for next_number in graph[number]['back']:
                    if next_number in visited or next_number == end_point:
                        continue
                    else:
                        visited.add(next_number)
                        home_can_come.add(next_number)
                        queue.append(next_number)


n, m = map(int, input().split())
route_inputs = [list(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

graph = {}

home_can_go = set()
home_can_come = set()
work_can_go = set()
work_can_come = set()

for i in range(1, n+1):
    graph[i] = {
        'front': set(),
        'back': set()
    }


for start, end in route_inputs:
    graph[start]['front'].add(end)
    graph[end]['back'].add(start)

bfs(deque([s]), t, 'front', {s,})
bfs(deque([s]), t, 'back', {s,})
bfs(deque([t]), s, 'front', {t,})
bfs(deque([t]), s, 'back', {t,})

print('home_can_go', home_can_go)
print('home_can_come', home_can_come)
print('work_can_go', work_can_go)
print('work_can_come', work_can_come)

print(len((home_can_go & work_can_come) & (home_can_come & work_can_go)))
