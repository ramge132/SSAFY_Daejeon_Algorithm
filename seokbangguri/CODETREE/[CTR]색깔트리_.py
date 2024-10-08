def check_depth(p_id, depth = 2):
    if p_id == -1:
        return True

    if nodes[p_id]['max_depth'] >= depth:
        return check_depth(nodes[p_id]['p_id'], depth + 1)
    
    return False


def update_colors(p_id, color):
    if p_id == -1:
        return
    
    nodes[p_id]['colors'][color-1] = 1
    update_colors(nodes[p_id]['p_id'], color)

# 노드 추가
def commandOne(code, m_id, p_id, color, max_depth):
    # 자식 노드가 추가 될 경우 부모노드의 max_depth보다 커지는 경우 추가 못함
    if p_id != -1 and not check_depth(p_id):
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
    update_parent_colors(p_id)

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
    

# 색 조회
def commandThree(code, m_id):
    return print(nodes[m_id]['color'])

# 점수 조회
def commandFour(code):
    result = 0
    for n in nodes.values():
        result += sum(n['colors'])**2

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