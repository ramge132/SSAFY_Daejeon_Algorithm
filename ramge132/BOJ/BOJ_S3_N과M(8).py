# https://www.acmicpc.net/problem/15657


# 1. 일반 버전 / 108 ms, 110556 KB
from itertools import combinations_with_replacement

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

# combinations_with_replacement 함수를 사용하여 중복을 허용하여 
# 길이 M인 비내림차순 수열 생성
sequences = combinations_with_replacement(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 108 ms, 113172 KB
def backtrack(start, sequence, numbers, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(start, N):
        sequence.append(numbers[i])
        backtrack(i, sequence, numbers, N, M)
        sequence.pop()

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

backtrack(0, [], numbers, N, M)
