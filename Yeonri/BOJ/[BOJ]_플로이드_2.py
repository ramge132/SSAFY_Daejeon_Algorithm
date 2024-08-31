N = int(input())
M = int(input())

# 거리와 경로 설정
dist = [[float('inf')] * N for _ in range(N)]
path = [[-1] * N for _ in range(N)]

for _ in range(M):
    s, e, w = map(int, input().split())
    if dist[s - 1][e - 1] > w:
        dist[s - 1][e - 1] = w
        path[s - 1][e - 1] = s - 1  # 이전 노드를 저장

# 플로이드-와샬 알고리즘을 통해 모든 경로의 최단 거리를 계산
for w in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][w] + dist[w][j]:
                dist[i][j] = dist[i][w] + dist[w][j]
                path[i][j] = path[w][j]

# 자신으로 가는 경로는 0으로 설정
for i in range(N):
    dist[i][i] = 0

# 최단 거리 행렬 출력
for i in range(N):
    for j in range(N):
        if dist[i][j] == float('inf'):
            dist[i][j] = 0
    print(*dist[i])

# 경로 생성
# 시작점과 목표 지점이 같아질 때 까지 반복
def get_path(i, j):
    result_path = []
    while j != i:
        result_path.append(j + 1) # 현재 노드를 추가
        j = path[i][j] # 현재 노드에 연결된 노드로 이동한다.
    result_path.append(i + 1) # 시작 노드를 경로에 추가.
    result_path.reverse() # 도착점 - > 시작점 이기 때문에 reverse를 사용하여 정렬
    return result_path

# 경로 출력
for i in range(N):
    for j in range(N):
        if dist[i][j] == 0 or i == j:
            print(0)
        else:
            result_path = get_path(i, j)
            print(len(result_path), " ".join(map(str, result_path)))