###########################################
# 직접 껐다 켰다 하는 방식 => 메모리 초과
###########################################
'''
from itertools import combinations_with_replacement

def press(x_pos):
    for y in range(N):
        temp_lamps[y][x_pos] = abs(temp_lamps[y][x_pos] - 1)

N, M = map(int, input().split())
lamps = [list(map(int, list(input()))) for _ in range(N)]
K = int(input())
result = 0

for switch in list(combinations_with_replacement(range(M), K)):
    if result == N:
        break

    temp_lamps = [a[:] for a in lamps]
    temp_switch = [switch.count(i)%2 for i in range(M)]
    temp_result = 0
    for i, x in enumerate(temp_switch):
        if x:
            press(i)

    for line in temp_lamps:
        if len(set(line)) == 1 and list(set(line))[0]:
            temp_result += 1
    
    if result < temp_result:
        result = temp_result

print(result)
'''
###########################################
# 켜야 하는 램프의 개수와 K를 맞추는 방법
###########################################
N, M = map(int, input().split())
lamps = [list(map(int, list(input()))) for _ in range(N)]
K = int(input())
same = set()
result = 0

for line in lamps:
    if tuple(line) in same:
        continue
    # 해당 행은 램프를 다 킬 수 있음
    lamps_counts = line.count(0)
    if lamps_counts%2 == K%2 and lamps_counts <= K:
        same.add(tuple(line))
        counts = lamps.count(line)
        if counts > result:
            result = counts

print(result)