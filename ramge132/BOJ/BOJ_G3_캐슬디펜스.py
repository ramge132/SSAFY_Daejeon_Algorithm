# https://www.acmicpc.net/problem/17135

from itertools import combinations
import copy

# 격자판의 행 수 N, 열 수 M, 궁수의 공격 거리 제한 D
N, M, D = map(int, input().split())

# 격자판의 상태 입력
grid = [list(map(int, input().split())) for _ in range(N)]

# 적의 위치를 찾는 함수
def get_enemies_positions(grid):
    positions = []
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 1:
                positions.append((r, c))
    return positions

# 적을 공격하는 함수
def attack(archers, grid):
    cnt = 0
    enemies = get_enemies_positions(grid)
    
    while enemies:
        targets = set()
        # 궁수들의 공격 처리
        for archer in archers:
            min_dist = D + 1
            target = None
            for enemy in enemies:
                dist = abs(enemy[0] - N) + abs(enemy[1] - archer)
                if dist <= D:
                    if dist < min_dist:
                        min_dist = dist
                        target = enemy
                    elif dist == min_dist and enemy[1] < target[1]:
                        target = enemy
            if target:
                targets.add(target)

        # 타겟들을 제거
        for target in targets:
            if target in enemies:
                enemies.remove(target)
                cnt += 1

        # 적 이동 처리
        enemies = [(r + 1, c) for r, c in enemies if r + 1 < N]

    return cnt

# 궁수 배치 조합 생성
max_kills = 0
for archers in combinations(range(M), 3):
    max_kills = max(max_kills, attack(archers, grid))

print(max_kills)