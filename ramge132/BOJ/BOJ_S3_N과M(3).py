# https://www.acmicpc.net/problem/15651


# 1. 일반 버전 / 396 ms, 113948 KB
from itertools import product

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

sequences = product(numbers, repeat=M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 456 ms, 115520 KB
def backtrack(sequence, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        sequence.append(i)
        backtrack(sequence, N, M)
        sequence.pop()

N, M = map(int, input().split())

backtrack([], N, M)
