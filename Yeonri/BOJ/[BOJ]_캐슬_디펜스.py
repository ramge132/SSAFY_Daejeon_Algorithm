from itertools import combinations

def chk_len(r_pos):
    min_len = float('inf')
    sel = -1  # 초기값을 -1로 설정하여 적이 선택되지 않았을 때를 처리
    for idx in range(len(enemy)):
        length = abs(enemy[idx][0] - r_pos[0]) + abs(enemy[idx][1] - r_pos[1])
        if D >= length:  # 궁수의 사정거리 내에 있는지 확인
            if min_len > length or (min_len == length and enemy[idx][1] < enemy[sel][1]):
                min_len = length
                sel = idx
    return sel  # 선택된 적의 인덱스를 반환, 선택된 적이 없으면 -1 반환

N, M, D = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]
max_total = 0

origin_enemy = [[i, j, 1] for i in range(N) for j in range(M) if lst[i][j] == 1]

for ranger in combinations(range(0, M), 3):
    total = 0
    enemy = [e[:] for e in origin_enemy]  # origin_enemy 리스트의 깊은 복사본 생성
    
    while len(enemy) > 0:        
        # 공격할 적 선택 및 제거
        to_remove = set()  # 제거할 적의 인덱스를 저장할 집합
        for i in ranger:
            sel_num = chk_len([N, i])
            if sel_num != -1:  # 선택된 적이 있는 경우
                to_remove.add(sel_num)
        
        # 적 제거
        for idx in to_remove:
            if enemy[idx][2] == 1:  # 적이 아직 살아있는지 확인
                enemy[idx][2] = 0
                total += 1
        
        # 적 이동
        tmp_idx = set()
        for enemy_idx in range(len(enemy)):
            if enemy[enemy_idx][2] == 0:
                tmp_idx.add(enemy_idx)

            else:
                enemy[enemy_idx][0] += 1
                if enemy[enemy_idx][0] == N:
                    tmp_idx.add(enemy_idx)

        # 적 제거 (큰 인덱스부터 제거)
        for kill_idx in sorted(tmp_idx, reverse=True):
            enemy.pop(kill_idx)

    max_total = max(max_total, total)

print(max_total)