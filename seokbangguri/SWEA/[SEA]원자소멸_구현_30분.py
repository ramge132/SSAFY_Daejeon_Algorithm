import sys
sys.stdin = open('input.txt')

# 상 하 좌 우
dxy = [[0, 0.5], [0, -0.5], [-0.5, 0], [0.5, 0]]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    # x 위치, y 위치, 이동방향, 보유 에너지
    energy = 0
    atoms = {}

    for _ in range(N):
        x, y, direction, egy = list(map(int, input().split()))
        if (x, y) not in atoms.keys():
            atoms[(x, y)] = []
        atoms[(x, y)].append([direction, egy])

    while atoms:
        temp_next_atoms = {}
        
        for key, value in atoms.items():
            cx, cy = key
            direction, egy = value[0]

            dx, dy = dxy[direction]
            nx, ny = cx + dx, cy + dy

            # 다음 좌표가 영역을 넘어가면 추가 X
            if nx < -1000 or nx > 1000 or ny < -1000 or ny > 1000:
                continue

            # 원자 위치 -> 키, 방향 및 에너지 -> 벨류
            temp_next_atoms.setdefault((nx, ny), []).append([direction, egy])

        next_atoms = {}

        for key, value in temp_next_atoms.items():
            # 동일 위치의 원자들 에너지를 추가하고 원자 삭제
            if len(value) > 1:
                energy += sum(val[1] for val in value)
            else:
                next_atoms[key] = value
        atoms = next_atoms

    print(f'#{test_case} {energy}')