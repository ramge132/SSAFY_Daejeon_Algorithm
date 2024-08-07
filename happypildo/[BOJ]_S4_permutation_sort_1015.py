"""
# 문제 설명
- 어떤 배열 A가 주어졌을 때, 또 다른 배열 P를 활용하여 정렬된 배열 B를 만들고자 한다.
- 여기서, P를 적용한다는 것은 `B[P[i]] = A[i]` 대입 연산을 진행한다는 것을 의미한다.
- A가 주어졌을 때, 정렬된 배열 B를 만들 수 있는 수열 P를 구하시오.

# 해피필도 팁
- 사실 sorted 써서 인덱스 추출하면 끝나는 문제이긴 하다.. 근데 공부하는거니까 한 번 써보았는데 복잡도가 크다 `O(N^2)`.
- 나중에 최대힙 같은 것을 잘 쓰게 된다면,,, 그걸 써서 풀어봐야겠다.
"""

N = int(input())

A = list(map(int, input().split()))
P = [float('inf') for n_iter in range(N)]

is_visited = set()
for iteration in range(N):
    current_min = float('inf')
    current_min_idx = float('inf')
    for i in range(N):
        if i in is_visited:
            continue
        if current_min > A[i]:
            current_min = A[i]
            current_min_idx = i

    P[current_min_idx] = iteration
    is_visited.add(current_min_idx)

answer = ""
for c in P:
    answer = answer + str(c) + " "
print(answer)