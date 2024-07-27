def checkVertical(l, x, y):
    if x > 0 and l[y][x-1]:
        x -= 1
        return goLeft(l, x, y)
    elif x < len(l[y]) - 1 and l[y][x+1]:
        x += 1
        return goRight(l, x, y)
    else:
        y -= 1
        return move(l, x, y)

def move(l, x, y, ):
    if y == 0:
        return x
    else:
        return checkVertical(l, x, y)

def goLeft(l, x, y, ):
    while x > 0 and l[y][x-1]:
        x -= 1
    y -= 1
    return move(l, x, y)
    
def goRight(l, x, y, ):
    while x < len(l[y]) - 1 and l[y][x+1]:
        x += 1
    y -= 1
    return move(l, x, y)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # test case number <- 이거때문에 한시간 잡아먹음
    t = int(input())
    # 사다리 2d matrix
    ladders = [list(map(int, input().split())) for _ in range(100)]
    # 현재 끝 점의 위치
    pointVertical = ladders[-1].index(2)
    poinHorizontal = len(ladders)-1

    print(f'#{t} {move(ladders, pointVertical, poinHorizontal)}')
    # ///////////////////////////////////////////////////////////////////////////////////