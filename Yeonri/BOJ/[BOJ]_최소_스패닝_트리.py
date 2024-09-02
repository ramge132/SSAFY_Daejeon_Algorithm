# 음수일 수 있다.
import heapq

mst = []
V, E = map(int, input().split())

adj_list = {v:[] for v in range(V)}

for _ in range(E):
    s, e, w = map(int, input().split())
    adj_list[s - 1].append((e - 1, w))
    adj_list[e - 1].append((s - 1, w))
    # 무방향 트리이기 때문에 양방향에 값을 추가했다.
    # 하지만, 1 < - > 2 일때, 2 -> 1로 가는 것을 체크하여 싸이클이 형성되었다.

visited = set()
init_v = 0
min_heap = [[w, init_v, e] for e, w in adj_list[init_v]]
heapq.heapify(min_heap)
visited.add(init_v)

while min_heap:
    weight, s, e = heapq.heappop(min_heap)
    if e in visited: continue
    visited.add(e)
    mst.append((s, e, weight))

    for adj_v, adj_w in adj_list[e]:
        if adj_v in visited: continue
        heapq.heappush(min_heap, [adj_w, e, adj_v])

result = 0
for i in range(len(mst)):
    result += mst[i][2]

print(result)