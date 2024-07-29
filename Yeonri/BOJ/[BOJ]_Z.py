N, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0
    
    # 2차원 배열의 크기 2**N
    # 2차원 배열을 사등분 2**(N-1)

    # 사등분한 배열에서 3번 배열에 존재하면
    # 1,2번 배열은 모두 방문을 하였기 때문에 2*[사등분한 배열의 크기]
    # 2 * half * half + z(N-1,r,c-half)
    # c - half를 하는 이유는 찾으려는 좌표의 절대 경로를 찾기 위해서이다.


    half = 2**(n-1)
    if r < half and c < half:
        return z(n-1, r, c)
    if r < half and c >= half:
        return half * half + z(n-1, r, c-half)
    if r >= half and c < half:
        return 2 * half * half + z(n-1, r-half, c)
    else:
        return 3 * half * half + z(n-1, r-half, c-half)

print(z(N, r, c))


# 먼저 2**N 길이를 가지는 배열을 생성한 후, 재귀 함수 N-1을 통해
# N=1을 만들어서 사각형 배열의 처음 부터 시작하려 했으나,
# 다음 사각형으로 이동해야 할 때를 구현하지 못함.

# 배열로 하는 것이 아니라, 주어진 r과 c의 위치를 기준으로
# 방문한 배열의 크기를 더한 후, 배열에서의 r, c 에 대한 절대좌표를 이용해
# 방문하기 까지 걸리는 횟수를 구하는 문제였다.