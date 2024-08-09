import sys
from collections import deque

def is_valid(nx, ny, N, M):
    return 0 <= nx < N and 0 <= ny < M

def bfs_shortest_path(grid, start, end):
    N = len(grid)
    M = len(grid[0])
    
    # 상하좌우 방향 정의
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    # 큐 초기화
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, dist = queue.popleft()
        
        if (x, y) == (end[0], end[1]):
            return dist
        
        for dx, dy in directions:
            nx, ny = x, y
            
            # 직진 가능한 만큼 이동
            temp_dist = dist
            while is_valid(nx + dx, ny + dy, N, M) and grid[nx + dx][ny + dy] == 0:
                nx += dx
                ny += dy
                temp_dist += 1
                
                # 도착지점에 도달하면 거리를 반환
                if (nx, ny) == (end[0], end[1]):
                    return temp_dist

            # 이미 방문하지 않은 좌표를 큐에 추가
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, temp_dist))
                    
    return -1  # 도착지에 도달할 수 없는 경우

# 입력 읽기
sys.stdin = open('algo2_sample_in.txt')
T = int(input())
for test_case in range(1, T + 1):
    M, N = map(int, input().split())
    route = [list(map(int, input().split())) for _ in range(M)]
    sx, sy, dx, dy = map(int, input().split())

    shortest_distance = bfs_shortest_path(route, (sx, sy), (dx, dy))
    print(f'#{test_case} {shortest_distance}')