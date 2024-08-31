import sys
sys.stdin = open('하나로.txt', 'r')

import heapq

# 환경 부담 세율: E * L(해저 터널 길이) ^ 2

# 현재 위치에서 가장 가까운 거리를 찾아서 이동하도록 설정하는 방법이 존재

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    adj_lst = {v: [] for v in range(N)}

    x_lst = list(map(int, input().split()))
    y_lst = list(map(int, input().split()))
    E = float(input())

    mst = []
    result = 0

    # 유클리드 거리 사용

    for i in range(N-1):
        for j in range(i+1, N):
            dist = ((x_lst[i] - x_lst[j])**2 + (y_lst[i] - y_lst[j])**2) ** 0.5
            adj_lst[i].append((j, E * dist ** 2))
            adj_lst[j].append((i, E * dist ** 2))
    
    visited = set()
    init_v = 0
    visited.add(init_v)
    min_heap = [[w, init_v, e] for e, w in adj_lst[init_v]]
    heapq.heapify(min_heap)

    while min_heap:
        w, s, e = heapq.heappop(min_heap)
        if e in visited: continue
        visited.add(e)

        for next_e, weight in adj_lst[e]:
            if next_e not in visited:
                heapq.heappush(min_heap, [weight, e, next_e])
        
        mst.append([s, e, w])
    
    for sel_mst in mst:
        result += sel_mst[2]

    print(f'#{test_case} {int(round(result))}')