import sys
sys.stdin = open('../../input.txt')
# sys.stdin = open('./000_study/input.txt')
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
        ['B', (None, 2, 1)],
        ['R', (None, 0, 0)],
        ['F', (None, 0, 0)],
        ['L', (None, 0, 1)]
    ],       # 변경 될 값 all : y = 0
    'D': [
        ['F', (None, 2, 0)],
        ['R', (None, 2, 1)],
        ['B', (None, 0, 1)],
        ['L', (None, 2, 0)]
    ],     # 변경 될 값 all : y = 2
    'F': [
        ['U', (None, 2, 0)],
        ['R', (0, None, 1)],
        ['D', (None, 0, 0)],
        ['L', (2, None, 1)]
    ],       # 변경 될 값 U : y = 2, R : x = 0, D : y = 0, L : x = 2
    'B': [
        ['U', (None, 0, 1)],
        ['L', (0, None, 0)],
        ['D', (None, 2, 1)],
        ['R', (2, None, 0)]
    ],        # 변경 될 값 U : y = 0, L : x = 0, D : y = 2, R : x = 2
    'L': [
        ['U', (0, None, 0)],
        ['F', (0, None, 0)],
        ['D', (0, None, 0)],
        ['B', (0, None, 0)]
    ],        # 변경 될 값 U : x = 0, F : x = 0, D : x = 0, B : x = 2
    'R': [
        ['U', (2, None, 0)],
        ['B', (2, None, 0)],
        ['D', (2, None, 0)],
        ['F', (2, None, 0)]
    ]        # 변경 될 값 U : x = 2, B : x = 0, D : x = 2, F : x = 2
}

# 돌리는 면의 인접한 면의 값을 바꾸는 함수
def rotateConnected(side, direction):
    temp_cube_val = []
    for s in connected[side]:
        temp = []
        # y 축 고정 x값
        if s[1][0] == None:
            for x in range(3):
                temp.append(cube[s[0]][s[1][1]][x])
            temp_cube_val.append(temp)
        # x 축 고정 y값
        else:
            for y in range(3):
                temp.append(cube[s[0]][y][s[1][0]])
            temp_cube_val.append(temp)
    
    for i, val in enumerate(temp_cube_val):
        # 시계방향
        if direction == '+':
            changed_color = connected[side][(i+1)%4]
            need_reverse = connected[side][i][1]
            if need_reverse[2]:
                val = val[::-1]
                if changed_color[1][0] == None:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][changed_color[1][1]][idx] = v
                else:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][idx][changed_color[1][0]] = v

            else:
                if changed_color[1][0] == None:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][changed_color[1][1]][idx] = v
                else:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][idx][changed_color[1][0]] = v

        # 반시계방향
        else:
            changed_color = connected[side][i-1]
            need_reverse = connected[side][i-1][1]
            if need_reverse[2]:
                val = val[::-1]
                if changed_color[1][0] == None:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][changed_color[1][1]][idx] = v
                else:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][idx][changed_color[1][0]] = v

            else:
                if changed_color[1][0] == None:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][changed_color[1][1]][idx] = v
                else:
                    for idx, v in enumerate(val):
                        cube[changed_color[0]][idx][changed_color[1][0]] = v


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
    cube = {}

    for key in default_color.keys():
        cube[key] = [[default_color[key]]*3 for _ in range(3)]
        # cube[key] = [[default_color[key]+str(i) for i in range(3)] for _ in range(3)]

    for side, direction in rotate:
        rotateCube(side, direction)

    for row in cube['U']:
        print(''.join(row))