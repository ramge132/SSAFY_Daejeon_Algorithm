# input
'''
3
.o. 1
o.. 1
..o 0
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    cups, k = map(str, input().split())
    for i,x in enumerate(cups):
        if x == 'o':
            cups = i
            break
    for _ in range(int(k)):
        if cups != 0:
            cups -= 1
        else:
            cups += 1
    print(f'#{test_case} {cups}')
    # ///////////////////////////////////////////////////////////////////////////////////
