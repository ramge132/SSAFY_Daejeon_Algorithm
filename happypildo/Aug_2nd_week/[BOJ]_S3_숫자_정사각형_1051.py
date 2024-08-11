"""
# 문제 설명:
- N x M 크기의 직사각형에 숫자들이 적혀 있다.
- 여기서, 각 꼭지점 숫자가 같은 정사각형을 찾고 싶다. 찾았다 치면, 그 정사각형들 중 가장 큰 정사각형의 사이즈는 몇인가?

# 접근법:
- 이딴게 문제?
- 내가 짠 코드가 복잡도가 `O(N^3)`이기는 하지만, 문제 상 `N, M <= 50`이기에, 복잡도가 그리 크지 않다.
- 그래서 brute-force로 풀기는 했지만, 사이즈가 가장 큰 것을 찾는 것이기 때문에 사이즈는 역순으로 돌렸다.
"""
def find_square_with_same_edge(rectangle_map, N, M):
    size_limit = min(N, M)
    for size in range(size_limit, 0, -1):
        for i in range(N):
            for j in range(M):
                if i+size-1 < N and j+size-1 < M:
                    if rectangle_map[i][j] == rectangle_map[i][j+size-1] == rectangle[i+size-1][j] == rectangle_map[i+size-1][j+size-1]:
                        return size

    return 1


N, M = list(map(int, input().split()))

rectangle = [input() for _ in range(N)]
print(find_square_with_same_edge(rectangle, N, M) ** 2)
