# https://www.acmicpc.net/problem/15650


# 1. 일반 버전 / 88 ms, 108080 KB
from itertools import combinations

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

sequences = combinations(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 84 ms, 108080 KB
def backtrack(start, sequence, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N + 1):
        sequence.append(i)
        backtrack(i + 1, sequence, N, M)
        sequence.pop()

N, M = map(int, input().split())

backtrack(1, [], N, M)
