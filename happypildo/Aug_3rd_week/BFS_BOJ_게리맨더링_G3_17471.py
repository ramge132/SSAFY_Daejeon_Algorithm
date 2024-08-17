from itertools import combinations
from collections import deque

def is_connected(graph, comb):
    if len(comb) == 1:
        return True

    # # DFS를 통해 연결성 여부를 판단
    # queue = deque([comb[0]])
    # is_visited = set([comb[0]])

    # while queue:
    #     item = queue.popleft()

    #     for neighbor in graph[item]:
    #         if neighbor in is_visited or neighbor not in comb:
    #             continue
    #         else:
    #             queue.append(neighbor)
    #             is_visited.add(neighbor)

    # BFS를 통해 연결성 여부를 판단
    queue = deque([comb[0]])
    is_visited = set([comb[0]])

    while queue:
        item = queue.pop()

        for neighbor in graph[item]:
            if neighbor in is_visited or neighbor not in comb:
                continue
            else:
                queue.append(neighbor)
                is_visited.add(neighbor)


    for elem in comb:
        if elem not in is_visited:
            return False
    return True

# Combination 반환 함수
def make_combinations_check(graph, population, total_population, arr):
    seen_before = set()
    min_gap = float('inf')

    for r in range(1, len(arr) // 2 + 1):
        for comb in combinations(arr, r):
            # 1. 연결성 여부 확인
            region_a = comb
            region_b = tuple([x for x in arr if x not in comb])

            # 이미 봤던 지역은 보지 않아도 된다.
            if region_a in seen_before or region_b in seen_before:
                continue
            else:
                seen_before.add(region_a)
                seen_before.add(region_b)

            if is_connected(graph, region_a) and is_connected(graph, region_b):
                # 연결 되어 있음 -> 인구수 계산 및 차이 갱신
                number_of_people_a = sum([x for idx, x in enumerate(population) if idx + 1 in region_a])
                number_of_people_b = total_population - number_of_people_a

                gap = abs(number_of_people_a - number_of_people_b)
                if min_gap > gap:
                    min_gap = gap
            else:
                continue
    
    if min_gap == float('inf'):
        return -1
    return min_gap


N = int(input())
population = list(map(int, input().split()))
total_population = sum(population)

graph = {}
for n_iter in range(1, N+1):
    input_arr = list(map(int, input().split()))
    graph[n_iter] = set(input_arr[1:])

# print("SOLUTION: ", make_combinations_check(graph, population, [x for x in range(1, N+1)]))
print(make_combinations_check(graph, population, total_population, [x for x in range(1, N+1)]))