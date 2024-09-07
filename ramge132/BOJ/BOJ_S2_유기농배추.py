# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수 정의
def dfs(x, y, M, N, field, visited):
    stack = [(x, y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))

def solve(T, test_cases):
    results = []
    
    for case in test_cases:
        M, N, K, positions = case
        # 배추밭과 방문 여부 초기화
        field = [[0] * N for _ in range(M)]
        visited = [[False] * N for _ in range(M)]
        
        # 배추 위치 입력
        for x, y in positions:
            field[x][y] = 1
        
        worm_count = 0
        
        # 배추밭을 순회하며 DFS 탐색
        for i in range(M):
            for j in range(N):
                if field[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, M, N, field, visited)
                    worm_count += 1

        results.append(worm_count)
    
    return results

T = int(input())  
test_cases = []

for _ in range(T):
    M, N, K = map(int, input().split()) 
    positions = [tuple(map(int, input().split())) for _ in range(K)]
    test_cases.append((M, N, K, positions))

results = solve(T, test_cases)

for result in results:
    print(result)
