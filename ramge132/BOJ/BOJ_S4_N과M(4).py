# https://www.acmicpc.net/problem/15652


# 1. 일반 버전 / 104 ms, 110564 KB
from itertools import combinations_with_replacement

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

# combinations_with_replacement 함수를 사용하여 
# 비내림차순으로 길이 M인 수열 생성
sequences = combinations_with_replacement(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 140 ms, 113027 KB
def backtrack(start, sequence, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N + 1):
        sequence.append(i)
        backtrack(i, sequence, N, M)
        sequence.pop()

N, M = map(int, input().split())

backtrack(1, [], N, M)
