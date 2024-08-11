"""
# 문제 설명
- 어떠한 양방향 순환 큐가 있고, 이 큐에서는 다음과 같은 연산을 할 수 있다.
    1. 첫 번째 원소를 뽑아낸다. (pop(0))
    2. 왼쪽으로 한 칸 옮긴다. 이 때, 첫번째에 있던 요소는 마지막 요소가 된다.
    3. 오른쪽으로 한 칸 옮긴다. 이 때, 마지막에 있던 요소는 첫번째 요소가 된다.
- 뽑아내고자 하는 원소의 위치가 있을 때, 이를 뽑아내기 위해 (2)와 (3)번 연산을 얼마나 해야하는가? (그 중 최소 값)

# 접근 방법
- 인덱싱 기법으로 접근했습니다. (python으로 푼다면, 쉽게 풀 수 있을 것이라 생각됩니다. (음수 인덱싱이 되기 때문에))
- 그래도 대가리 박고자 하지 않았읍니다...

# 팁
- 수업때문에 머릿속에 DFS밖에 없어서 다 찾으려다가 2^50 경우의수를 확인하고 접었습니다. 이상입니다.
"""

N, M = list(map(int, input().split()))
target_arr = list(map(int, input().split()))
target_arr = [x - 1 for x in target_arr]

answer = 0
hit = 0
while len(target_arr) > 0:
    target = target_arr[0]

    left = target
    right = (N - hit) - target

    _ = target_arr.pop(0)

    hit = hit + 1
    if left < right:
        answer = answer + left

        temp = []
        for t in target_arr:
            t = t - left - 1
            if t < 0:
                t = t + (N - hit) + 1
            temp.append(t)
        target_arr = temp
    else:
        answer = answer + right

        temp = []
        for t in target_arr:
            t = t + right - 1
            if t > (N - hit) - 1:
                t = t - (N - hit + 1)
            temp.append(t)
        target_arr = temp

print(answer)