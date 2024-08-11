# https://www.acmicpc.net/problem/2606

def dfs(graph, start, visited):
    visited[start] = True
    count = 1  # 현재 컴퓨터도 감염되었으므로 1로 시작

    for next_computer in graph[start]:
        if not visited[next_computer]:
            count += dfs(graph, next_computer, visited)

    return count

n = int(input())  # 컴퓨터의 수
m = int(input())  # 네트워크 상에서 직접 연결된 컴퓨터 쌍의 수

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 여부 확인 리스트 초기화
visited = [False] * (n + 1)

# 1번 컴퓨터를 통해 감염된 컴퓨터의 수 계산 (1번 컴퓨터 제외)
infected_count = dfs(graph, 1, visited) - 1

print(infected_count)
