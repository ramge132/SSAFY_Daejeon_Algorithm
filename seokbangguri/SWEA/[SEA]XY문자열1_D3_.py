#input
'''
3
Y
XYYX
XY
XYY
X
YY
'''
def tracking(a, n):
    while n > 0:
        if a[-1] == 'X':
            a = a[:-1]
            n -= 1
        elif a[-1] == 'Y':
            a = a[::-1][1:]
            n-=1
    return a

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    s = input()
    e = input()
    n = len(e) - len(s)
    if s == tracking(e, n):
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
    # ///////////////////////////////////////////////////////////////////////////////////
