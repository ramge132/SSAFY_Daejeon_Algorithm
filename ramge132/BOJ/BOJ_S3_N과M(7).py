# https://www.acmicpc.net/problem/15656


# 1. 일반 버전 / 524 ms, 112484	KB
from itertools import product

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = product(sorted(numbers), repeat=M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 612 ms, 115336 KB
def backtrack(sequence, numbers, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(N):
        sequence.append(numbers[i])
        backtrack(sequence, numbers, N, M)
        sequence.pop()

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

backtrack([], numbers, N, M)
