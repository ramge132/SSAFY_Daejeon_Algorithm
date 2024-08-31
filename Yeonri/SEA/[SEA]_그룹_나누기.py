import sys
sys.stdin = open('그룹나누기.txt', 'r')

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    parent = [i for i in range(N+1)]

    for i in range(0, len(lst), 2):
        union(parent, lst[i], lst[i+1])

    groups = set()
    for i in range(1, N+1):
        groups.add(find(parent, i))

    result = len(groups)
    
    print(f'#{test_case} {result}')

# import sys
# sys.stdin = open('그룹나누기.txt', 'r')

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))

#     per = 0
#     visited = set()

#     for i in range(0, len(lst), 2):
#         if lst[i] not in visited and lst[i + 1] not in visited:
#             visited.add(lst[i + 1])
#             visited.add(lst[i])
#             per += 1
#         elif lst[i] not in visited or lst[i + 1] not in visited:
#             visited.add(lst[i + 1])
#             visited.add(lst[i])
#         else:
#             continue

#     for i in range(1, N+1):
#         if i not in visited:
#             per += 1

#     print(f'#{test_case} {per}')


# import sys
# sys.stdin = open('그룹나누기.txt', 'r')

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))

#     per = 0
#     visited = []

#     for i in range(0, len(lst), 2):
#         if i in visited and i + 1 in visited: continue
#         per += 1
    
#     result = N - per
    
#     print(f'#{test_case} {result}')


# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))
#     print(f'#{test_case} {N - len(lst) // 2}')

# T = int(input())

# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     lst = list(map(int, input().split()))

#     per = 0
#     visited = []

#     for i in range(0, len(lst), 2):
#         if i in visited and i + 1 in visited: continue
#         per += 1
    
#     result = N - per
    
#     print(f'#{test_case} {result}')