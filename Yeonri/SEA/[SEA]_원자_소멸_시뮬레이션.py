import sys
sys.stdin = open('원자소멸시뮬레이션.txt', 'r')

T = int(input())

DXY = [(0, 1), (0, -1), (-1, 0), (1, 0),]

for test_case in range(1, T + 1):
    N = int(input())
    
    # 기존의 lst는 리스트를 input으로 받은 후, 다시 for문을 이용해서 atom_dict에 다시 저장을 해야한다.

    atom_dict = {}
    total = 0

    for i in range(N):
        x, y, dir, energy = list(map(int, input().split()))
        current_pos = (2 * x, 2 * y)
        if current_pos not in atom_dict:
            atom_dict[current_pos] = []
        atom_dict[current_pos].append((dir, energy))

    # atom_dict에 값들을 저장
    # 왜? 2중 for문을 이용해서 값을 비교하지 않고, dict를 이용해서 같은 좌표일 때, value의 길이를 이용한다.

    while atom_dict:
        tmp_dict = {}

        # atom_dict에 저장된 값들을 이용해서 충돌 원자를 확인해야 한다.
        for (x, y), atoms in atom_dict.items():
            # 같은 위치에 존재하는 원자가 2개 이상일 때,
            if len(atoms) >= 2:
                # 전부 저장
                total += sum(k for d, k in atoms) # atoms에 들어있는 d, k 중 k만 저장
                # 충돌한 원자는 tmp_dict에 저장하지 않는다.
                continue

            d, k = atoms[0]
            dx, dy = DXY[d] # atoms[0]이 방향
            cx, cy = (x, y)
            nx, ny = cx + dx, cy + dy

            # 원자 충돌이 안일어나는 경우
            if -2000 >= nx or 2000 <= nx or -2000 >= ny or 2000 <= ny: continue
            tmp_dict.setdefault((nx, ny), []).append((d, k))

        atom_dict = tmp_dict

    print(f'#{test_case} {total}')
        


    # x, y를 저장하고, 방향과 원자를 저장하도록 만든다.
    # {(x,y) : (DXY, energe)}
    # 만약 같은 좌표에 원자가 두개 이상 존재하면, {(x,y) : (DXY, energe), (DXY, energe)}




