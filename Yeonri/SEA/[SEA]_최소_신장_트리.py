import sys
sys.stdin = open('최소신장트리.txt', 'r')
import heapq

T = int(input())


for test_case in range(1, T + 1):
    LAST_V, E = map(int, input().split())

    mst = []
    result = 0

    adj_list = {v:[] for v in range(LAST_V + 1)} # 인접 리스트를 생성

    for _ in range(E): # 간선의 개수 만큼 인접 리스트에 정보들을 저장한다.
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w)) # 시작 부분
        adj_list[e].append((s, w)) # 끝 부분
    
    visited = set()
    init_v = 0 # 해당 문제에서 정점의 처음은 0 부터 시작하기 때문에 0으로 설정하였음
    visited.add(init_v) # 초기 방문 정점
    min_heap = [[w, init_v, e] for e, w in adj_list[init_v]]
    heapq.heapify(min_heap) # 최소 힙으로 생성한다.

    while min_heap:
        w, s, e = heapq.heappop(min_heap)
        if e in visited: continue # e를 방문하였을 때, 건너뜀

        visited.add(e)
        # 선택된 e에 연결된 노드들을 min_heap에 저장한다.
        for next_e, weight in adj_list[e]:
            if next_e not in visited:
                heapq.heappush(min_heap, [weight, e, next_e]) # 현재 e에 연결된 다음 노드 (next_e)
        
        mst.append([s, e, w])

    for sel_mst in mst:
        result += sel_mst[2]

    print(f'#{test_case} {result}')
