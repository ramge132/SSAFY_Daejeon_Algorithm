default_color = {
    'U': 'w',
    'D': 'y',
    'F': 'r',
    'B': 'o',
    'L': 'g',
    'R': 'b'
}

connected = {
    'U': [
        ['B', (None, 0)],
        ['R', (None, 0)],
        ['F', (None, 0)],
        ['L', (None, 0)]
    ],       # 변경 될 값 all : y = 0
    'D': [
        ['F', (None, 2)],
        ['R', (None, 2)],
        ['B', (None, 2)],
        ['L', (None, 2)]
    ],     # 변경 될 값 all : y = 2
    'F': [
        ['U', (None, 2)],
        ['R', (0, None)],
        ['D', (None, 0)],
        ['L', (2, None)]
    ],       # 변경 될 값 U : y = 2, R : x = 0, D : y = 0, L : x = 2
    'B': [
        ['U', (None, 0)],
        ['L', (0, None)],
        ['D', (None, 2)],
        ['R', (2, None)]
    ],        # 변경 될 값 U : y = 0, L : x = 0, D : y = 2, R : x = 2
    'L': [
        ['U', (0, None)],
        ['F', (0, None)],
        ['D', (0, None)],
        ['B', (2, None)]
    ],        # 변경 될 값 U : x = 0, F : x = 0, D : x = 0, B : x = 2
    'R': [
        ['U', (2, None)],
        ['B', (0, None)],
        ['D', (2, None)],
        ['F', (2, None)]
    ]        # 변경 될 값 U : x = 2, B : x = 0, D : x = 2, F : x = 2
}

# 돌리는 면의 인접한 면의 값을 바꾸는 함수
def rotateConnected(side, direction):
    temp_cube_val = [cube[connected_side] for connected_side, val_index in connected[side]]
    '''

    수정 중

    '''
    pass

# 돌리는 면을 돌리는 함수
def rotateCube(side, direction):
    # 시계방향
    if direction == '+':
        cube[side] = [list(row)[::-1] for row in zip(*cube[side])]

        rotateConnected(side, direction)

    # 반시계방향
    else:
        cube[side] = [list(row) for row in zip(*cube[side])][::-1]

        rotateConnected(side, direction)

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    rotate = list(map(lambda x: list(x), input().split()))
    print(rotate)
    cube = {}

    for key in default_color.keys():
        cube[key] = [[default_color[key]]*3 for _ in range(3)]

    for side, direction in rotate:
        rotateCube(side, direction)

    print(cube)