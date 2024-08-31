import sys
sys.stdin = open('최소이동거리.txt', 'r')

import heapq
T = int(input())

for test_case in range(1, T+1):
    N, E = map(int, input().split())

    graph = {v:{} for v in range(N+1)}

    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w

    distance = [float('inf')] * (N + 1)
    distance[0] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, 0]) # weight, vertex

    while min_heap:

        current_w, current_v = heapq.heappop(min_heap)
        for vertex, weight in graph[current_v].items(): # 현재 선택한 정점에 연결된 인접 정점
            if distance[vertex] > weight + distance[current_v]:
                distance[vertex] = weight + distance[current_v]
                heapq.heappush(min_heap, [distance[vertex], vertex])


    print(f'#{test_case} {distance[-1]}')