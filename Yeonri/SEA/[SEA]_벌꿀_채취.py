import sys
from itertools import combinations
sys.stdin = open('벌꿀채취.txt', 'r')

T = int(input())

# main
# 2명의 사람이 각자 벌통을 선택하여 해당 값 중 최대 값을 가질 수 있도록 만든다.
# 1번 사람이 먼저 벌통을 선택한다.
# 2번 사람은 1번 사람이 선택한 벌통 이외의 벌통을 선택한다.

# dfs
# 벌통을 모두 탐색해야 하므로, <선택할 때, 선택하지 않을 때> 2번의 dfs를 진행한다.
# 선택한 벌통의 합이 C를 초과 하지 않는지 확인
# 위의 과정으로 선별된 벌통의 합이 저장된 최대 값과 비교
# dfs 진행 중 C보다 높은 sum(total)이 존재할 때, 정답이 나올 수 없기 때문에 종료한다.

# num: 벌통을 선택한 사람 번호
# i,j:  선택한 벌통의 위치
# cnt: 벌통을 선택할 수 있는 값인 M을 비교하는 카운트
# total: 선택한 벌통의 총 값 -> list로 만들어서 선택된 벌통의 값들을 저장한다. -> 벌통의 값들을 C와 비교해야 하기 때문

def dfs(num, i, j, cnt, total): 
    global honey_a_val, honey_b_val
    
    current_total = sum(total)
    result = 0

    for k in total:
        result += k ** 2
    
    if current_total > C:
        return

    if cnt == M:
        if num == 1 and result > honey_a_val:
            honey_a_val = result

        elif num == 2 and result > honey_b_val:
            honey_b_val = result

        return

    dfs(num, i, j+1, cnt + 1, total + [lst[i][j]]) # 선택한다.
    dfs(num, i, j+1, cnt + 1, total) # 선택하지 않는다.
    

for test_case in range(1, T + 1):

    ans = []

    N, M, C = map(int,input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]


    for i in range(N):
        for j in range(N-M+1):
            honey_a_val = 0 
            dfs(1, i, j, 0, []) # 1번째 사람이 선택한 벌통

            for i2 in range(i, N):
                for j2 in range(N-M+1):
                    if i == i2 and j + M - 1 >= j2: continue # 같은 라인이고, 첫번 째 사람이 선택한 벌통의 마지막 위치가 두번째 사람이 선택한 첫번째 벌통의 위치가 겹치지 않을 때
                    honey_b_val = 0
                    dfs(2, i2, j2, 0, []) # 2번째 사람이 선택한 벌통
                    ans.append(honey_a_val + honey_b_val) # dfs에서 honey_(a,b)_val에 값들이 저장되기 때문에 반복문이 돌 때 마다 0으로 값을 초기화 해줘야 한다.
    
    print(f'#{test_case} {max(ans)}')

# 전역 변수로 honey_a_val, honey_b_val을 지정해서 for문이 실행되서 선택되는 순서에 관계없이
# a의 최댓값, b의 최댓값이 저장되어서 이전에 실행했던 값인 b와 현재 실행된 a가 더해지는 오류가 발생
# for문을 돌 때 마다 값들이 0으로 초기화 되도록 설정하였다.

# ans.append()의 위치 또한 중요하다. for문 밖에 저장을 하면 ans 값은 맨 마지막 값이 저장된다.