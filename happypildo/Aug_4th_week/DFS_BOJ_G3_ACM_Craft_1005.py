"""
# 문제 설명
- ACM Craft라는 게임은 건물을 짓는 게임이다.
- 이에 대한 규칙은 아래와 같다.
    - X Y는 Y 건물을 짓기 위해서는 X 건물이 선행되어야 함을 의미한다.
    - 건물을 지을 때는 시간이 걸리는데, 어떠한 (선행 조건을 만족한) 두 개 이상의 건물을 동시에 지을 수 있다.
- 이러한 규칙이 주어질 때, 타겟 건물을 짓기 위해 얼마의 최소 시간이 필요한지 구하라.

# 접근 방법
- Dependency graph라는 변수를 생성하여 어떤 건물을 짓기 위해 필요한 건물이 무엇인지 표시했습니다.
- 이후, 타겟 건물을 기준으로 DFS를 수행하고 그 때의 최대 딜레이를 계산했습니다.
    - 여기서, 시간 초과가 났었는데 MEMOIZATION을 구성하여 해결했습니다.
## MEMOIZATION이 필요한 이유
```
1 2
1 3
2 4
3 4
```
- 위 예시 건물 순서에 따라 한다면, 1번 건물 계산을 두 번 하게 됩니다.
- 입력 예시가 매우 큰데, 이 중 당연히 겹치는 건물이 생기게 될 것이고 이를 MEMOIZATION으로 해결했습니다.
"""

highest_delay = -1
MEMOIZATION = {}
def DFS(delay_list, graph, start_point):
    global highest_delay
    global MEMOIZATION

    if MEMOIZATION.get(start_point, None) is not None:
        return MEMOIZATION[start_point]
    
    delay = delay_list[start_point - 1]
    ret = []
    for neighbor in graph[start_point]:
        ret.append(DFS(delay_list, graph, neighbor))
    
    if len(ret) == 0:
        MEMOIZATION[start_point] = delay
    else:
        ret = [item + delay for item in ret]
        delay = max(ret)
        MEMOIZATION[start_point] = delay
    return MEMOIZATION[start_point]

T = int(input())

for t_iter in range(1, T+1):
    highest_delay = -1
    MEMOIZATION = {}
    N, K = list(map(int, input().strip().split()))

    build_delay = list(map(int, input().strip().split()))

    dependency_graph = {x+1: set() for x in range(N)}
    for k_iter in range(K):
        from_building, to_building = list(map(int, input().split()))
        dependency_graph[to_building].add(from_building)
    target_building = int(input())

    DFS(build_delay, dependency_graph, target_building)
    print(MEMOIZATION[target_building])