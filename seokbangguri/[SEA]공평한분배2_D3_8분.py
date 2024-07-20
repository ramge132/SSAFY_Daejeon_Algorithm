# input
'''
3
3 2
1 2 3
3 3
5 20 10
4 3
4 3 2 1
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    candies.sort()
    minimun = []
    for i in range(n-k+1):
        max_c = candies[i:k+i][-1]
        min_c = candies[i:k+i][0]
        minimun.append(max_c - min_c)
    print(f'#{test_case} {min(minimun)}')
    # ///////////////////////////////////////////////////////////////////////////////////
