class DisjointSet:
    def __init__(self, N):
        self.parent = [0] * (N + 1)
        self.rank = [0] * (N + 1)
    
    def make_set(self, item):
        self.parent[item] = item

    def find_set(self, item):
        if item != self.parent[item]:
            self.parent[item] = self.find_set(self.parent[item])
        return self.parent[item]
    
    def union_set(self, A, B):
        A_parent = self.find_set(A)
        B_parent = self.find_set(B)

        if A_parent != B_parent:
            if self.rank[A_parent] > self.rank[B_parent]:
                # 작은 애가 들어가야 한다.
                self.parent[B_parent] = A_parent
            elif self.rank[A_parent] < self.rank[B_parent]:
                self.parent[A_parent] = B_parent
            else:
                self.parent[A_parent] = B_parent
                self.rank[B_parent] += 1


T = int(input())
for t_iter in range(1, T+1):
    N, M = list(map(int, input().split()))
    
    ds = DisjointSet(N)
    for n in range(1, N + 1):
        ds.make_set(n)

    pairs = list(map(int, input().split()))
    for idx in range(0, M * 2, 2):
        A = pairs[idx]
        B = pairs[idx + 1]
        ds.union_set(A, B)
    
    for n in range(1, N + 1):
        _ = ds.find_set(n)
        
    print(f"#{t_iter} {len(set(ds.parent)) - 1}")