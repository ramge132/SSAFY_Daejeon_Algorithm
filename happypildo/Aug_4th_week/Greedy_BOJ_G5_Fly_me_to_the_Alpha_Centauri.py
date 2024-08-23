"""
# 문제 설명:
- 알파 센타우리라는 우주선은 특이하게 속도를 바꾸려면, [현재 속도 - 1, 현재 속도, 현재 속도 + 1]로만 변경 가능하다.
- 또한, 목적지 도착 직전에 속도는 1이여야 한다.
- 이 우주선을 타고 갈 때, X에서 Y로 가고자 한다.
    - 몇 번 속도를 바꿔야, 최소한으로 바꿀 수 있는지 출력하시오.
- 예시)
    - 1에서 5로 간다고 해보자.
    - 가능한 정답은 3번으로
        - 속도: [1, 2, 1]
"""
SUMMATION_DICT = {}

def make_summation_dict():
    global SUMMATION_DICT
    s = 0
    SUMMATION_DICT[-1] = 0
    for i in range(0, 50000):
        s += i
        SUMMATION_DICT[i] = s

def solve(curr_X, Y):
    global SUMMATION_DICT
    # ret = [0]
    curr_speed = 0
    depth = 0
    while curr_X != Y:
        if Y - (curr_X + (curr_speed + 1)) >= SUMMATION_DICT[curr_speed]:
            # 속도를 하나 증가해도 된다.
            curr_speed += 1
        elif Y - (curr_X + (curr_speed)) >= SUMMATION_DICT[curr_speed - 1]:
            pass
        else:
            if curr_speed - 1 > 0:
                curr_speed -= 1
        curr_X += curr_speed

        depth += 1
        # ret.append(curr_speed)

    # print(ret)
    return depth


make_summation_dict()
T = int(input())
for t_iter in range(T):
    X, Y = list(map(int, input().split()))

    answer = solve(X, Y)

    print(answer)