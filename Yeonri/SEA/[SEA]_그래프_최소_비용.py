import sys
sys.stdin = open('그래프최소비용.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    graph = [list(map(int, input().split())) for _ in range(N)] 
    dist = [[float('inf')] *N for _ in range(N)]

    result = 0

    for i in range(N):
        dist[i][i] = 0
    
    for u in range(N):
        for v in range(N):
            if graph[u][v]!=0:
                dist[u][v] = graph[u][v]

    for k in range(N):
        for u in range(N):
            for v in range(N):
                distance = dist[u][k] + dist[k][v]
                if dist[u][v] > distance:
                    dist[u][v] = distance

    for i in range(N):
        result = max(result, max(dist[i]))

    print(f'#{test_case} {result}')
