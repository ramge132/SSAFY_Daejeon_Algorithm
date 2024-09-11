# dfs를 먼저 돌려서 첫번째로 찾은 노드들을 visited에 저장을 한다.
# 탐색을 하지 못한 노드에 대해서 bfs를 돌린다.
# 만약 visited에 도달하지 못한 노드가 존재할 때, return을 시킨다.

# DFS로 탐색한 노드에 대해서 해당 노드로 이동할 수 있는 노드들을 저장해서 BFS를 돌려본다.
from collections import deque

def bfs(start, lst, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        
        for item in lst[current]:
            if visited[item] == True: continue
            visited[item] = True
            queue.append(item)


N, M = map(int, input().split())

adj_list = {v:[] for v in range(N)}
adj_re = {v:[] for v in range(N)}

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s - 1].append(e - 1)
    adj_re[e - 1].append(s - 1) # 역방향을 설정해서 정방향에서 방문을 제대로 했는지 체크를 한다.

start, end = map(int, input().split())

start -= 1
end -= 1

cnt = 0

visited = [False] * (N + 1)

# start을 선택해서 다음 순서로 이동해서 end까지
# end를 선택해서 다음 순서로 이동해서 start까지

# print(adj_list)

visited_start = [False] * (N + 1)
bfs(start, adj_list, visited_start)

visited_end = [False] * (N + 1)
bfs(end, adj_list, visited_end)

re_visited_start = [False] * (N + 1)
bfs(start, adj_re, re_visited_start)

re_visited_end = [False] * (N + 1)
bfs(end, adj_re, re_visited_end)

for i in range(len(adj_list)):
    if i == start or i == end: continue
    if visited_start[i] and visited_end[i] and re_visited_start[i] and re_visited_end[i]:
        cnt += 1

# print(s_set)
# print(e_set)
print(cnt)
print(visited_start)
print(visited_end)
print(re_visited_start)
print(re_visited_end)
# 글로벌 visited 변수를 만들어서 각 숫자의 인덱스별로 횟수를 나타내에 방문 여부를 확인한다. 
# -> 속도차이 0.3초 ~~ 0.02초
# 데이터가 많은 케이스의 경우일 수록 속도의 차이가 없어지는 것 같다.

# def chk(i, dir, num):
#     global cnt, s_set, e_set
    
#     # print(dir)
#     # print(i)

#     if visited[i] > 1:
#         return
    

#     if i == end and num == 0:
#         print(dir)
#         s_set = s_set | dir
#         return
    
#     elif i == start and num == 1:
#         print(dir)
#         e_set = e_set | dir
#         return

#     for item in adj_list[i]:
        
#         if i in dir:
#             visited[i] += 1
#             dir.add(i)
#             chk(item, dir, num)
#             visited[i] -= 1
#         else:
#             dir.add(i)
#             chk(item, dir, num)


# N, M = map(int, input().split())

# adj_list = {v:[] for v in range(N)}

# for _ in range(M):
#     s, e = map(int, input().split())
#     adj_list[s - 1].append(e - 1)

# start, end = map(int, input().split())

# start -= 1
# end -= 1

# s_set = set()
# e_set = set()

# cnt = 0

# visited = [0] * (N + 1)

# # start을 선택해서 다음 순서로 이동해서 end까지
# # end를 선택해서 다음 순서로 이동해서 start까지

# # print(adj_list)

# chk(start, set(), 0)
# chk(end, set(), 1)


# # print(s_set)
# # print(e_set)
# print(len(s_set & e_set))


# visited 인자를 설정하여 방문 여부를 체크하도록 만든다.

# def chk(i, dir, visited, num):
#     global cnt
    
#     print(dir)
#     print(i)

#     if i in visited:
#         return

#     if i == end and num == 0:
#         for i in range(1, len(dir)):
#             s_set.add(dir[i])
#         return
    
#     elif i == start and num == 1:
#         for i in range(1, len(dir)):
#             e_set.add(dir[i])
#         return

#     for item in adj_list[i]:
#         if i in dir:
#             chk(item, dir + [i], visited + [i], num)
#         else:
#             chk(item, dir + [i], visited, num)

# N, M = map(int, input().split())

# adj_list = {v:[] for v in range(N)}

# for _ in range(M):
#     s, e = map(int, input().split())
#     adj_list[s - 1].append(e - 1)

# start, end = map(int, input().split())

# start -= 1
# end -= 1

# s_set = set()
# e_set = set()

# cnt = 0

# # start을 선택해서 다음 순서로 이동해서 end까지
# # end를 선택해서 다음 순서로 이동해서 start까지

# # print(adj_list)

# chk(start, [], [], 0)
# chk(end, [], [], 1)

# # print(s_set & e_set)
# print(len(s_set & e_set))