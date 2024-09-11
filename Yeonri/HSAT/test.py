from collections import deque

def chk(i, num):
    global cnt, s_set, e_set, s_visited, e_visited

    dir = set()
    queue = deque([i])

    while queue:
        # print(dir)
        i = queue.popleft()

        if i != start and i != end and num == 0:
            s_visited[i] = True
            dir.add(i)

        if i != start and i != end and num == 1:
            e_visited[i] = True
            dir.add(i)

        
        if i == end and num == 0:
            s_set = s_set | dir
            continue
        
        elif i == start and num == 1:
            e_set = e_set | dir
            continue

        for item in adj_list[i]:
            if i in dir:
                visited[i] += 1
                queue.append(item)
            else:
                queue.append(item)

    return dir

    

N, M = map(int, input().split())

adj_list = {v:[] for v in range(N)}

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s - 1].append(e - 1)

start, end = map(int, input().split())

start -= 1
end -= 1

s_visited = [False] * (N)
e_visited = [False] * (N)

s_set = set()
e_set = set()

cnt = 0


# start을 선택해서 다음 순서로 이동해서 end까지
# end를 선택해서 다음 순서로 이동해서 start까지


# print(adj_list)
visited = [0] * (N + 1)
s_set = chk(start, 0)

visited = [0] * (N + 1) # visited를 초기화 해줘야 한다.
e_set = chk(end, 1)

# print(s_set & e_set)
print(len(s_set & e_set))

print(s_visited)
print(e_visited)



# from collections import deque

# def chk(i, num):
#     global cnt, s_set, e_set

#     dir = set()
#     queue = deque([i])

#     while queue:
#         # print(dir)
#         i = queue.popleft()

#         if i != start and i != end:
#             dir.add(i)

#         # if visited[i] > 4:
#         #     continue
        

#         if i == end and num == 0:
#             s_set = s_set | dir
#             continue
        
#         elif i == start and num == 1:
#             e_set = e_set | dir
#             continue

#         for item in adj_list[i]:
#             if i in dir:
#                 visited[i] += 1
#                 queue.append(item)
#             else:
#                 queue.append(item)

#     return dir

    

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
# visited = [0] * (N + 1)
# s_set = chk(start, 0)

# visited = [0] * (N + 1) # visited를 초기화 해줘야 한다.
# e_set = chk(end, 1)

# # print(s_set & e_set)
# print(len(s_set & e_set))