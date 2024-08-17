"""
# 문제 설명
- 배추에 어떤 벌레를 놓으면 그 벌레는 상하좌우로 퍼져 나가게 된다.
- 모든 배추에 그 벌레가 퍼지길 바랄 때, 최소 몇 마리의 배추를 놓으면 되는가?

# 접근 방법
- 기본적인 BFS 기법입니다.
- 먼저 배추이 상하좌우로 연결되었는지를 표현하는 그래프를 형성하고 (`make_graph()`)
- 모든 배추 위치에서 BFS를 호출하여 방문하지 않을 경우만 1을 반환하도록 했습니다. (`BFS()`)
    - 다른 배추의 BFS로 인해 방문된 배추라면 0을 반환
- 즉, 그래프의 수를 세는 문제였습니다.
"""

from collections import deque

DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def make_graph(locations, farm, N, M):
    graph = {}
    
    for loc in locations:
        graph[loc] = set()

    for loc in locations:
        x, y = loc

        for dx, dy in DIRECTION:
            if (-1 < x + dx < M) and (-1 < y + dy < N):
                if farm[x+dx][y+dy] == 1:
                    graph[loc].add((x+dx, y+dy))
                    graph[(x+dx, y+dy)].add(loc)

    return graph


def BFS(graph, start_node, is_visited):
    if start_node in is_visited:
        return 0, is_visited
    else:
        queue = deque([start_node])
        is_visited.add(start_node)

        while queue:
            item = queue.popleft()

            for neighbor in graph[item]:
                if neighbor not in is_visited:
                    is_visited.add(neighbor)
                    queue.append(neighbor)

        return 1, is_visited


T = int(input())

for t_iter in range(T):
    M, N, K = list(map(int, input().split()))

    loc_of_lec = []
    farm = [[0 for n_iter in range(N)] for m_iter in range(M)]

    for _ in range(K):
        x, y = list(map(int, input().split()))
        farm[x][y] = 1
        loc_of_lec.append((x, y))

    graph = make_graph(loc_of_lec, farm, N, M)

    answer = 0
    is_visited = set()
    for start_node in loc_of_lec:
        ret, is_visited = BFS(graph, start_node, is_visited)
        answer += ret
    
    print(answer)
