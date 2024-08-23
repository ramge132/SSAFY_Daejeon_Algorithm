# https://www.acmicpc.net/problem/17471

from itertools import combinations
from collections import deque

# 구역의 개수 입력
N = int(input())

# 각 구역의 인구 입력
population = list(map(int, input().split()))

# 구역의 연결 정보 입력
adj_list = [[] for _ in range(N)]
for i in range(N):
    data = list(map(int, input().split()))
    adj_list[i] = [x - 1 for x in data[1:]]  # 인덱스를 0부터 시작하도록 조정

# 연결된 그룹인지 확인하는 함수 (BFS를 이용)
def is_connected(group):
    if not group:
        return False
    queue = deque([group[0]])
    visited = set([group[0]])
    
    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if neighbor in group and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return len(visited) == len(group)

# 가능한 모든 조합을 시도
min_diff = float('inf')
for i in range(1, N // 2 + 1):
    for comb in combinations(range(N), i):
        group_a = list(comb)
        group_b = [x for x in range(N) if x not in group_a]  # 조건 수정
        
        if is_connected(group_a) and is_connected(group_b):
            pop_a = sum(population[x] for x in group_a)
            pop_b = sum(population[x] for x in group_b)
            min_diff = min(min_diff, abs(pop_a - pop_b))

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)