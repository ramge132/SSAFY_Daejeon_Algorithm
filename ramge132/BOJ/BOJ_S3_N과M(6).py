# https://www.acmicpc.net/problem/15655


# 1. 일반 버전 / 92 ms, 108080 KB
from itertools import combinations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = combinations(sorted(numbers), M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 92 ms, 108080 KB
def backtrack(start, sequence, numbers, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N):
        sequence.append(numbers[i])
        backtrack(i + 1, sequence, numbers, N, M)
        sequence.pop()

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

backtrack(0, [], numbers, N, M)
