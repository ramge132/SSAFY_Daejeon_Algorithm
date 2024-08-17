"""
# 문제 링크
- https://www.acmicpc.net/problem/1080

# 문제 설명
- 0과 1로만 구성된 행렬 A와 B가 있다. A에 X연산을 진행하여 B를 만들기 위해 몇 번의 연산이 필요한지 출력하라
- X연산은 3X3 크기의 모든 원소를 뒤집는 것이다 (즉, 0->1, 1->0)

# 접근 방법
- 완전 탐색이 머릿속에 먼저 나왔으나, 최대 연산 횟수가 2^(50 * 50)이라 다른 방법이 있나 생각해 보았습니다.
- 모든 점을 하나 씩 순서대로 돌면서 flip의 경우의 수를 셀 때,
    - 내가 지난 점은 절대 바뀌지 않게 되기에,
    - 내가 있는 점이 B와 다르다면 무조건 flip해야 한다는 것을 깨달았습니다.
- 접근은 Greedy를 사용해서 했다고 보면 될 것 같습니다.
"""
def flip(A, N, M, i, j):
    if (-1 < i + 3 - 1 < N) and (-1 < j + 3 - 1 < M):
        for di in range(3):
            for dj in range(3):
                if A[i+di][j+dj] == 1:
                    A[i+di][j+dj] = 0
                else:
                    A[i+di][j+dj] = 1
        
        return A, 1
    else:
        return A, 0

def greedily_flip(A, B, N, M):
    ret = 0

    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                A, is_flipped = flip(A, N, M, i, j)
                ret += is_flipped

    if A == B:
        return ret
    else:
        return -1


N, M = list(map(int, input().split()))

A = []
B = []
for n_iter in range(N):
    line = input()
    A.append([int(x) for x in line])
for n_iter in range(N):
    line = input()
    B.append([int(x) for x in line])

print(greedily_flip(A, B, N, M))