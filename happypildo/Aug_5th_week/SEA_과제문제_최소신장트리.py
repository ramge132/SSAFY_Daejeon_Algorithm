import time

class DisjointSet:
    def __init__(self, V):
        self.p = [0] * V
        self.r = [0] * V
    
    def make_set(self, val):
        # 처음에는 자기 자신을 부모로 삼는다.
        # 자기 자신이 대표자이다.
        self.p[val] = val

    def find_set(self, val):
        # val이 속한 집합의 대표자를 찾아 보자.
        # 자기 자신이 대표자가 아니라면
        if val != self.p[val]:
            # 대표자를 찾기 위해 재귀적으로 진행, 대표자를 찾으면 그 값을 지정
            self.p[val] = self.find_set(self.p[val])
        return self.p[val]

    def union(self, x, y):
        # x 와 y를 합쳐주자.

        # 일단 각자 대표자가 누구인지 확인해야 함
        rep_x = self.find_set(x)
        rep_y = self.find_set(y)

        if rep_x != rep_y:
            # 두 집합이 서로소 집합이여야 함
            if self.r[rep_x] > self.r[rep_y]:
                # 랭크가 작은 값이 붙어야 편향 방지 가능
                self.p[rep_y] = rep_x
            elif self.r[rep_x] < self.r[rep_y]:
                self.p[rep_x] = rep_y
            else:
                self.p[rep_x] = rep_y
                self.r[rep_y] += 1


def kruskal(vertex, edges, ds):
    mst = []
    sorted_edges = sorted(edges, key= lambda x: x[2])

    ans = 0
    cnt = 0
    while len(mst) < len(vertex) - 1:
        s, e, w = sorted_edges[cnt]
        if ds.find_set(s) != ds.find_set(e):
            ds.union(s, e)
            mst.append((s, e, w))
            ans += w

        cnt += 1

    return ans

import heapq
def prim(vertex, edges):
    adj_list = {x: [] for x in vertex}
    for s, e, w in edges:
        adj_list[s].append((w, e))
        adj_list[e].append((w, s))
    
    ans = 0
    visited = set()
    init_vertex = vertex[0]
    min_heap = [val for val in adj_list[init_vertex]]

    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        if len(visited) > len(vertex):
            break
        # print("Heap info: ", min_heap)
        w, e = heapq.heappop(min_heap)
        # print("\t -> To go: ", (e, w))
        if e in visited: continue

        visited.add(e)
        ans += w

        for adj_w, adj_v in adj_list[e]:
            if adj_v not in visited:
                # print("\t -> Next: ", (adj_v, adj_w))
                heapq.heappush(min_heap, (adj_w, adj_v))


    return ans
            
start_time = time.time()
T = int(input())

for t_iter in range(1, T+1):
    V, E = list(map(int, input().split()))

    vertex = [i for i in range(V + 1)]
    edges = [list(map(int, input().split())) for e in range(E)]

    # ds = DisjointSet(V + 1)
    # for v in range(V + 1):
    #     ds.make_set(v)
    
    # print(f"#{t_iter} {kruskal(vertex, edges, ds)}")
    print(f"#{t_iter} {prim(vertex, edges)}")

end_time = time.time()
print(end_time - start_time)

"""
0.9107611179351807
0.8275012969970703
0.73
0.78
"""

"""
1.0232892036437988
0.86
0.92
0.83
"""

