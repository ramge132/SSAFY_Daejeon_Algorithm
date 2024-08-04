import sys
from itertools import combinations
sys.stdin = open('요리사.txt', 'r')


def get_score(arr, lst):
    sum_lst = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            x, y = arr[i], arr[j]
            sum_lst += lst[x][y] + lst[y][x]
    return sum_lst


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    SELECT = N // 2  # 식재료 선택 개수

    food_combi = list(combinations(range(N), SELECT))

    combi_score = {}
    for combi in food_combi:
        combi_score[combi] = get_score(combi, lst)

    ans = float('inf')
    food_idx = [i for i in range(N)]

    for sel in food_combi:
        sel2 = tuple(num for num in food_idx if num not in sel)
        sel_sum = combi_score[sel]
        sel2_sum = combi_score[sel2]
        ans = min(ans, abs(sel_sum - sel2_sum))

    print(f'#{test_case} {ans}')

'''import sys
sys.stdin = open('요리사.txt', 'r')

def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1: yield [arr[i]]
        else:
            for next in combinations(arr[i+1:], r-1):
                yield [arr[i]] + next

def get_score(arr):
    sum_lst = 0
    combi_lst = combinations(arr, 2)

    for combi in combi_lst:
        x, y = combi
        sum_lst += lst[x][y] + lst[y][x]

    return sum_lst

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    SELECT = N // 2 # 식재료 선택 개수
    ans = float('inf')
    food_combi = []
    food_idx = [i for i in range(N)] # 조합에 사용할 인덱스 추출
    # 섞인 재료는 사용할 수 없다.
    # 음식의 시너지가 작은 것이 답

    food_combi += combinations(food_idx, SELECT) # 조합 추출

    # dict에 존재하는 값을 하나 가져와서 겹치지 않는 key 값을 가져오고 싶다.
    # 다른 방법?

    # dict를 sel1는 기존에 만든 food_dict를 사용
    # sel2는 dict를 따로 만든다.

    for sel in food_combi:
        sel2 = [num for num in food_idx if num not in sel]

        sel_sum = get_score(sel)
        sel2_sum = get_score(sel2)

        ans = min(ans, abs(sel_sum - sel2_sum))

    print(f'# {test_case} {ans}')'''