# https://www.acmicpc.net/problem/15654


# 1. 일반 버전 / 160 ms, 116192 KB
from itertools import permutations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sequences = permutations(numbers, M)

for sequence in sorted(sequences):
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 160 ms, 112300 KB
def backtrack(sequence, visited, numbers, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sequence.append(numbers[i])
            backtrack(sequence, visited, numbers, N, M)
            sequence.pop()
            visited[i] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

visited = [False] * N

backtrack([], visited, numbers, N, M)
