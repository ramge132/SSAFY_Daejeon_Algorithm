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

    temp_visited = {}

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