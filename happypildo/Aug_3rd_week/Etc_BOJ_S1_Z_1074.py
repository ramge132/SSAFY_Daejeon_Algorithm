"""
# 문제 링크
- https://www.acmicpc.net/problem/1074

# 문제 설명
- 크기가 2^N by 2^N인 2차원 배열을 Z모양으로 탐색을 진행한다.
    - N = 1일 경우, 
        [[1, 2], [3, 4]] 배열을 1, 2, 3, 4로 탐색한다.
    - N = 2일 경우,
        [[0, 1, 4, 5], [2, 3, 6, 7], [8, 9, 12, 13], [10, 11, 14, 15]]  배열을 1~15순으로 탐색한다.
    - 자세한 설명은 링크 참고
- 이 때, (r, c) 위치의 값을 언제 탐색하는지 순서를 출력하시오.

# 접근 방법
- 재귀를 연습하기 좋은 문제라고 생각합니다.
- 매 재귀 호출 시, 배열을 4개의 부분으로 나누어 인덱싱 처리를 함으로써 문제를 풀었습니다.
"""
def recursively_check_index(N, r, c):
    if N == 0:
        return 0
    if (-1 < r < 2 ** (N - 1)) and (-1 < c < 2 ** (N - 1)):
        return 0 + recursively_check_index(N - 1, r, c)    
    elif (-1 < r < 2 ** (N - 1)) and (2 ** (N - 1) <= c < 2 ** N):
        return (2 ** (N - 1)) ** 2 + recursively_check_index(N - 1, r, c - 2 ** (N - 1))
    elif (2 ** (N - 1) <= r < 2 ** N) and (-1 < c < 2 ** (N - 1)):
        return (2 ** (N - 1)) ** 2 * 2 + recursively_check_index(N - 1, r - 2 ** (N - 1), c)
    elif (2 ** (N - 1) <= r < 2 ** N) and (2 ** (N - 1) <= c < 2 ** N):
        return (2 ** (N - 1)) ** 2 * 3 + recursively_check_index(N - 1, r - 2 ** (N - 1), c - 2 ** (N - 1))
    
N, r, c = list(map(int, input().split()))
print(recursively_check_index(N, r, c))