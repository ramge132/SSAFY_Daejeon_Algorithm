N = int(input())

M = int(input())

# dist 설정
# dist 초기 설정은 N * N에 대해서 float('inf')로 설정한다.
dist = [[float('inf')] * N for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    dist[s - 1][e - 1] = min(dist[s - 1][e - 1], w)


for w in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][w] + dist[w][j])

for i in range(N):
    dist[i][i] = 0
    for j in range(N):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0

for i in range(N):
    print(*dist[i])