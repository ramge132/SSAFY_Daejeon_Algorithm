# https://www.acmicpc.net/problem/15649


# 1. 일반 버전 / 128 ms, 110824 KB
from itertools import permutations

N, M = map(int, input().split())

numbers = list(range(1, N + 1))

sequences = permutations(numbers, M)

for sequence in sequences:
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 148 ms, 112144 KB
def backtrack(sequence, visited, N, M):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            sequence.append(i)
            backtrack(sequence, visited, N, M)
            sequence.pop()
            visited[i] = False

N, M = map(int, input().split())

visited = [False] * (N + 1)

backtrack([], visited, N, M)
