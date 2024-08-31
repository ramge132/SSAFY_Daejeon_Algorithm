# https://www.acmicpc.net/problem/11726

def tile_ways(n):
    # 방법의 수를 저장할 배열 초기화
    ways = [0] * (n + 1)
    
    # 초기값 설정
    ways[1] = 1
    if n > 1:
        ways[2] = 2
    
    # DP 테이블 채우기
    for i in range(3, n + 1):
        ways[i] = (ways[i-1] + ways[i-2]) % 10007
    
    return ways[n]

n = int(input())
print(tile_ways(n))
