import sys
from itertools import combinations
sys.stdin = open('input.txt')

# 접근 방식
'''
선택할 수 있는 모든 벌통을 구하고 조합을 이용해서 조건에 맞는 합이 가장 큰 경우를 계산
'''
prints = ''
T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    honey_list = []
    result = 0

    for y in range(N):
        for x in range(N-M+1):
            temp = matrix[y][x:x+M]
            temp.append([x, y, sum(temp)])
            honey_list.append(temp)

    for first, second in combinations(honey_list, 2):
        # 바로 옆 트레이인 경우
        if first[-1][1] == second[-1][1] and first[-1][0] + M > second[-1][0]:
            continue

        # 첫번째에서 추출 할 수 있는 꿀의 양
        temp_first = 0
        if first[-1][-1] <= C:
            temp_first = sum(x**2 for x in first[:M])
        
        else:
            for i in range(M-1, 0, -1):
                for val in combinations(first[:M], i):
                    if sum(val) <= C and temp_first < sum(x**2 for x in val):
                        temp_first = sum(x**2 for x in val)

        # 두번째에서 추출 할 수 있는 꿀의 양
        temp_second = 0
        if second[-1][-1] <= C:
            temp_second = sum(x**2 for x in second[:M])
        
        else:
            for i in range(M-1, 0, -1):
                for val in combinations(second[:M], i):
                    if sum(val) <= C and temp_second < sum(x**2 for x in val):
                        temp_second = sum(x**2 for x in val)

        # 추출 꿀이 현재 최대보다 큰 경우
        if result < temp_first + temp_second:
            result = temp_first + temp_second
    
    prints += f'#{test_case} {result}'

print(prints)