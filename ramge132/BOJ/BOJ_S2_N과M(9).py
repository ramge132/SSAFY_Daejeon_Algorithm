# https://www.acmicpc.net/problem/15663


# 1. 일반 버전 / 132 ms, 113820 KB
from itertools import permutations

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

# 입력받은 수를 정렬
numbers.sort()

# 순열을 저장할 집합을 초기화
unique_sequences = set()

# permutations 함수를 사용하여 모든 순열을 생성
for sequence in permutations(numbers, M):
    unique_sequences.add(sequence)

# 집합에 저장된 순열을 사전 순으로 정렬하여 출력
for sequence in sorted(unique_sequences):
    print(' '.join(map(str, sequence)))


###############################################


# 2. 백트래킹 버전 / 148 ms, 117832 KB
def backtrack(depth, sequence):
    if depth == M:
        result.add(tuple(sequence))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            sequence.append(numbers[i])
            backtrack(depth + 1, sequence)
            sequence.pop()
            visited[i] = False

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

result = set()

visited = [False] * N

backtrack(0, [])

for sequence in sorted(result):
    print(' '.join(map(str, sequence)))
