import heapq

def prim(islands, E):
    ans = 0

    is_visited = set()
    init_island = 0
    is_visited.add(init_island)
    min_heap = []

    island = islands[init_island]
    for idx, distance in enumerate(island[2:]):
        min_heap.append((distance * E, idx))

    heapq.heapify(min_heap)
    while min_heap:
        # print(min_heap)
        w, e = heapq.heappop(min_heap)
        if e in is_visited: continue
        is_visited.add(e)
        ans += w

        island = islands[e]
        for idx in range(len(islands)):
            if idx == e or idx in is_visited: continue
            heapq.heappush(min_heap, (island[2 + idx] * E, idx))
    
    return ans


T = int(input())
for t_iter in range(1, T+1):
    N = int(input())
    islands = {x: [0, 0] + [float('inf') for _ in range(N)] for x in range(N)}
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    
    idx=0
    for x, y in zip(X, Y):
        islands[idx][0] = x
        islands[idx][1] = y
        idx += 1
    
    E = float(input())

    for n_iter in range(N):
        for dn_iter in range(N):
            if n_iter == dn_iter: continue
            islands[n_iter][2 + dn_iter] = (islands[n_iter][0] - islands[dn_iter][0]) ** 2 + (islands[n_iter][1] - islands[dn_iter][1]) ** 2
            # print((islands[n_iter][0] - islands[dn_iter][0]) ** 2 + (islands[n_iter][1] - islands[dn_iter][1]) ** 2)

    answer = prim(islands, E)
    print(f"#{t_iter} {round(answer)}")