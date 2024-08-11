"""
# 문제 설명
- N개의 스위치 정보가 0 또는 1로 주어진다.
- 그리고 학생들에게 숫자를 주는데 이는 다음과 같다.
    - 남학생(1)의 경우, 자신이 받은 숫자의 배수에 해당하는 스위치를 toggle 한다.
    - 여학생(2)의 경우, 자신이 받은 숫자를 기준으로 양 옆에 스위치의 모습이 대칭된다면 최대로 대칭되는 범위의 스위치들을 toggle

# 접근 방법
- 큰건 없고 그냥 풀었읍니다.
"""
def toggle(val):
    if val == 0: return 1
    else: return 0


def boy_switch(switches, num):
    cnt = 1

    while num * cnt < len(switches):
        switches[num * cnt] = toggle(switches[num * cnt])

        cnt += 1

    return switches


def girl_switch(switches, num):
    start = num - 1
    end = num + 1

    while (0 < start < len(switches)) and (0 < end < len(switches)):
        if switches[start] == switches[end]:
            start -= 1
            end += 1
        else:
            break
    start += 1
    end -= 1
    
    for offset in range(start, end + 1):
        switches[offset] = toggle(switches[offset])

    return switches


N = int(input())
switches = [-1] + list(map(int, input().split()))
M = int(input())

for m_iter in range(M):
    gender, number = list(map(int, input().split()))

    if gender == 1:
        switches = boy_switch(switches, number)
    elif gender == 2:
        switches = girl_switch(switches, number)

result = ""
for idx in range(1, len(switches)):
    result += str(switches[idx]) + " "
    if idx % 20 == 0:
        result += "\n"
print(result)
