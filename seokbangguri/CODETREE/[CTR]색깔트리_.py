'''

15
100 1 -1 1 3
100 2 1 2 1
100 3 2 3 2
400
100 4 1 1 3
100 5 4 3 2
400
200 4 4
100 6 4 5 2
300 1
300 5
300 6
400
200 2 4
400


6
100 1 -1 1 3
100 2 1 2 2
100 3 1 3 1
100 4 3 4 1
300 2
400


'''

# from pprint import pprint

def update_colors(p_id, color):
    if p_id == -1:
        return
    
    nodes[p_id]['colors'][color-1] = 1
    update_colors(nodes[p_id]['p_id'], color)

    pass

# 노드 추가
def commandOne(code, m_id, p_id, color, max_depth):
    # 자식 노드가 추가 될 경우 부모노드의 max_depth보다 커지는 경우 추가 못함
    if p_id != -1 and (len(nodes[p_id]['child_node_mids']) + 2) // 2 + 1 > nodes[p_id]['max_depth']:
        return

    # 자식 노드 생성
    nodes[m_id] = {
        'p_id': p_id,
        'color': color,
        'max_depth': max_depth,
        'current_depth': 1,
        'child_node_mids': [],
        'colors': [0]*5
    }
    nodes[m_id]['colors'][color-1] = 1

    if p_id != -1:
        # 부모 노드의 자식 노드 리스트에 추가
        nodes[p_id]['child_node_mids'].append(m_id)
        # 부모 노드가 가지고 있는 colors 업데이트
        update_colors(p_id, color)
        # 부모 노드 current_depth 새로 계산
        nodes[p_id]['current_depth'] = (len(nodes[p_id]['child_node_mids']) + 1) // 2 + 1

def update_parent_colors(m_id):
    if m_id == -1:
        return
    
    p_id = nodes[m_id]['p_id']

    if p_id == -1:
        return

    temp_colors = [0]*5
    temp_colors[nodes[p_id]['color']-1] = 1

    for child_mid in nodes[p_id]['child_node_mids']:
        for i, x in enumerate(nodes[child_mid]['colors']):
            if x:
                temp_colors[i] = 1

    nodes[p_id]['colors'] = temp_colors
    update_parent_colors(nodes[p_id]['p_id'])

# 색 변경
def commandTwo(code, m_id, color):
    # 서브 트리의 루트 노드 색 변경
    nodes[m_id]['color'] = color
    nodes[m_id]['colors'] = [0]*5
    nodes[m_id]['colors'][color-1] = 1

    # 루트 노드의 자식 노드들 색 변경
    for child_mid in nodes[m_id]['child_node_mids']:
        commandTwo(200, child_mid, color)

    return m_id

    # 부모 노드의 색 변경
    '''
    
    부모 노드가 가지고 있는 색들을 변경해줘야함 그럼 끝
    
    '''

    

# 색 조회
def commandThree(code, m_id):
    return print(nodes[m_id]['color'])

# 점수 조회
def commandFour(code):
    result = 0
    for n in nodes.values():
        # pprint(n)
        result += sum(n['colors'])**2

    # return print('result', result)
    return print(result)


Q = int(input())
commands = [list(map(int, input().split())) for _ in range(Q)]

nodes = {}

for c in commands:
    if c[0] == 100:
        commandOne(*c)
    elif c[0] == 200:
        m_id = commandTwo(*c)
        update_parent_colors(m_id)
    elif c[0] == 300:
        commandThree(*c)
    elif c[0] == 400:
        commandFour(*c)

# pprint(nodes)