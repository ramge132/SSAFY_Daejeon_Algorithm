from collections import deque


def BFS(network):
    queue = deque()
    is_visited = set()

    queue.append(1)
    is_visited.add(1)

    infected = 0
    while queue:
        current_com = queue.popleft()

        for neighbor in graph[current_com]:
            if neighbor not in is_visited:
                queue.append(neighbor)
                is_visited.add(neighbor)
                infected += 1

    return infected


num_of_computers = int(input())
num_of_links = int(input())

graph = {x+1: set() for x in range(num_of_computers)}
for l_iter in range(num_of_links):
    X, Y = list(map(int, input().split()))
    graph[X].add(Y)
    graph[Y].add(X)

answer = BFS(graph)
print(answer)
    