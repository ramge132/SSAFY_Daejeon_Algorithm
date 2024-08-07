"""
N x M의 미로에 갇혀 있다. 출발지는 (1, 1)이고 탈출지는 (N, M)이다.
0은 가로막혀 있는 부분이며, 1은 갈 수 있는 길이다.
미로는 반드시 탈출할 수 있는 형태라고 할 때, 탈출 시 이동할 수 있는 최소 칸의 개수를 구하시오.
"""
from collections import deque

DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def BFS(maze, start_point, end_point, N, M):
    queue = deque([start_point])
    cost_map = [[float('inf') for m_iter in range(M)] for n_iter in range(N)]
    cost_map[start_point[0]][start_point[1]] = 1

    while queue:
        current_point = queue.popleft()
        current_x = current_point[0]
        current_y = current_point[1]

        for direction in DIRECTION:
            temp_x = current_point[0] + direction[0]
            temp_y = current_point[1] + direction[1]
            temp_point = (temp_x, temp_y)

            if (-1 < temp_x < N) and (-1 < temp_y < M) and maze[temp_x][temp_y] != '0':
                new_cost = cost_map[current_x][current_y] + int(maze[temp_x][temp_y])
                original_cost = cost_map[temp_x][temp_y]

                if new_cost < original_cost:
                    cost_map[temp_x][temp_y] = new_cost
                    queue.append(temp_point)

    if cost_map[end_point[0]][end_point[1]] == float('inf'):
        return -1
    else:
        return cost_map[end_point[0]][end_point[1]]
    

N, M = list(map(int, input().split()))
maze = [input() for n_iter in range(N)]

start_point = (0, 0)
end_point = (N-1, M-1)

answer = BFS(maze, start_point, end_point, N, M)
print(answer)