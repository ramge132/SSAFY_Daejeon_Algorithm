# 각 노드 특정 색깔
# 최대 깊이
# 동적으로 노드 추가, 색깔 변경
# 고유 번호 m, 부모 노드 번호 p, 색깔 , 최대 깊이
# 빨 주 노 초 파 12345
# p id -1 새로운 트리의 루트 노드

from collections import defaultdict

def create_node(content):
    global graph, re_graph
    # 부모 노드의 깊이보다 현재 노드의 깊이가 크면 안됨 > 같거나 작다.
    if content[2] == -1:
        graph[content[1]] = content[2:]
        re_graph[content[2]] = content[1]

    else:
        # 부모들을 찾아 이동해서 값을 탐색한다.
        create_flag = True
        next_id = content[2]

        if graph[next_id][2] < content[-1]: # 부모노드의 깊이보다 클 경우 오류
            create_flag = False
    
        if create_flag:
            graph[content[1]] = content[2:]
            re_graph[content[2]].append(content[1])

def change_color(current_id, col):
    global graph

    # 입력된 값에 대한 모든 자식 노드에 적용해야 된다.
    # 현재 노드의 색 변경
    graph[current_id][1] = col

    if current_id not in re_graph:
        return
    
    next_id = re_graph[current_id]

    for id in next_id:
        change_color(id, col)

    # 양쪽에 자식 노드가 존재하기 때문에 dfs를 이용한다.
    # while True:

    #     # 현재 노드와 연결된 자식 노드의 번호를 찾는다.
        
    #     # 연결된 자식 노드가 존재하지 않을 때,
    #     if current_id not in re_graph:
    #         break
        
    #     next_id = re_graph[current_id]

    #     graph[next_id][1] = content[2]
        
    #     current_id = next_id

def check_color(content):
    print(graph[content[1]][1])


# def total_score(current_id, sel_color, cnt):
#     global total

#     print(f'current_id: {current_id} / sel_color: {sel_color} / cnt: {cnt} / total: {total}')
    
#     if graph[current_id][1] != sel_color:
#         cnt += 1

#     if current_id not in re_graph:
#         total += (cnt ** 2)
#         # print(f'current_id: {current_id} / sel_color: {sel_color} / total: {total}')
#         return
    
#     next_id = re_graph[current_id]

#     for id in next_id:
#         total_score(id, sel_color, cnt)

def total_score(current_id, sel_color):
    global total, cnt

    print(f'current_id: {current_id} / sel_color: {sel_color} / cnt: {cnt} / total: {total}')
    
    if graph[current_id][1] != sel_color:
        cnt += 1

    if current_id not in re_graph:
        # print(f'current_id: {current_id} / sel_color: {sel_color} / total: {total}')
        return
    
    next_id = re_graph[current_id]

    for id in next_id:
        total_score(id, sel_color)

Q = int(input())

graph = defaultdict(list)
re_graph = defaultdict(list)

lst = []
total = 0
cnt = 0

for _ in range(Q):
    lst.append(list(map(int, input().split())))

for content in lst:
    if content[0] == 100:
        create_node(content)

    if content[0] == 200:
        # 현재 선택된 노드 ID와 변경할 색깔 
        change_color(content[1], content[2])

    if content[0] == 300:
        check_color(content)

    if content[0] == 400:
        total = 0
        # 루트 노드부터 시작
        current_id = re_graph[-1]

        # 모든 노드에 대해서 dfs를 실행하여 점수를 계산
        for current_id in graph:
            cnt = 0
            sel_color = graph[current_id][1]
            # 현재 위치한 노드 번호, 초기 색상, 다른 색상의 개수
            total_score(current_id, sel_color)
            total += (cnt ** 2)
        
        print(total)

print(graph)
print(re_graph)