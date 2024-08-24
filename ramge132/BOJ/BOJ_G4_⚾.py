# https://www.acmicpc.net/problem/17281

from itertools import permutations

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]

# 가능한 타순을 계산하기 위해 1번 선수를 4번 타자로 고정
players = [i for i in range(1, 9)]

def simulate(order):
    score = 0
    current_player = 0
    
    for inning in innings:
        bases = [0, 0, 0]  # 1루, 2루, 3루 상태
        outs = 0
        
        while outs < 3:
            result = inning[order[current_player]]
            if result == 0:  # 아웃
                outs += 1
            else:
                # 점수 계산
                if result == 1:
                    score += bases[2]
                    bases = [1] + bases[:2]
                elif result == 2:
                    score += bases[1] + bases[2]
                    bases = [0, 1] + bases[:1]
                elif result == 3:
                    score += bases[0] + bases[1] + bases[2]
                    bases = [0, 0, 1]
                elif result == 4:
                    score += bases[0] + bases[1] + bases[2] + 1
                    bases = [0, 0, 0]

            # 다음 타자로 이동
            current_player = (current_player + 1) % 9

    return score

# 1번 선수를 4번 타자로 고정하고, 나머지 순열 생성
max_score = 0
for perm in permutations(players):
    order = list(perm[:3]) + [0] + list(perm[3:])
    max_score = max(max_score, simulate(order))

print(max_score)