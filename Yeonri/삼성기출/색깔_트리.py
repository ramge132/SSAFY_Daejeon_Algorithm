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
        re_graph[content[2]].append(content[1])

    else:
        # 부모들을 찾아 이동해서 값을 탐색한다.
        create_flag = True
        next_id = content[2]

        create_flag = count_depth(next_id, 2)
        
        if create_flag:
            graph[content[1]] = content[2:]
            re_graph[content[2]].append(content[1])

def count_depth(current_id, cnt):

    parent_id =  graph[current_id][0]

    # 현재 깊이보다 cnt가 작을 때, 실패
    if graph[current_id][2] < cnt:
        return False

    # print(current_id, graph[current_id], parent_id, cnt)
    if parent_id == -1:
        return True
    
    return count_depth(parent_id, cnt + 1)

    
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

def check_color(content):
    print(graph[content[1]][1])


# 각 노드의 색상과 점수가 중복되어 저장되는 문제가 발생
# 각 노드에대한 색상 저장과 total_score를 구하는 함수를 분리

# 선택된 노드에 연결된 자식들의 고유 색상을 저장후 반환
def calculate_value(current_id):
    colors = set([graph[current_id][1]])

    if current_id not in re_graph:
        return colors

    for child_id in re_graph[current_id]:
        child_colors = calculate_value(child_id)
        colors.update(child_colors)
    
    return colors

# 각 노드에 대한 고유 색상값을 가져와서 점수 계산
def total_score():
    total = 0
    for node_id in graph:
        value = len(calculate_value(node_id))
        total += value ** 2
    return total

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
        print(total_score())

# print(graph)
# print(re_graph)
