# import sys
# sys.stdin = open('input.txt')

# 정지 상 하 좌 우 [x, y]
dxy = [[0, 0], [0, -1], [0, 1], [-1, 0], [1, 0]]

def microbe_moves(microbes, times):
    global m
    if times == m:
        return
    
    # 군집 이동시키기
    for i, x in enumerate(microbes):
        # 비활성화 된 군집은 건너뜀
        if x[-1] == 0:
            continue

        microbes[i][1] += dxy[x[3]][0] 
        microbes[i][0] += dxy[x[3]][1]
        
        # 가장자리 군집 절반으로 줄이기 및 방향 바꾸기
        if microbes[i][1] == 0 or microbes[i][1] == n - 1 or microbes[i][0] == 0 or microbes[i][0] == n - 1:
            # 방향이 홀수 인 경우
            if microbes[i][3]%2:
                microbes[i][3] += 1
            # 짝수 인 경우
            else:
                microbes[i][3] -= 1
            
            # 개채 수 줄이기
            microbes[i][2] = int(microbes[i][2] / 2)

    # 같은 셀에 위치 시 미생물 수 합치고 가장 큰 군집의 이동방향 따르기
    find_same_pos = {}
    for idx, microbe in enumerate(microbes):
        # 비활성화 된 군집은 건너뜀
        if microbe[-1] == 0:
            continue

        pos_to_str = tuple(microbe[:2])
        if pos_to_str in find_same_pos:
            find_same_pos[pos_to_str].append(microbe + [idx])
        else:
            find_same_pos[pos_to_str] = [microbe + [idx]]

    # 같은 셀에 있는 군집들 중 가장 군집이 많은 리스트에 남은 군집들 추가하고 남은 군집들 비활성화
    for value in find_same_pos.values():
        if len(value) > 1:
            max_index = max(range(len(value)), key=lambda i: value[i][2])
            max_value_list = value[max_index]

            # 나머지 리스트들의 인덱스 2의 값을 가장 큰 값을 가진 리스트의 인덱스 2의 값에 더하고 비활성화
            for i, row in enumerate(value):
                if i != max_index:
                    microbes[max_value_list[-1]][2] += row[2]
                    microbes[row[-1]][-1] = 0
    
    microbe_moves(microbes, times + 1)

T = int(input())
for test_case in range(1, T + 1):
    # 셀의 한 변, 시간, 군집 개수
    n, m, k = map(int, input().split())
    # [1] <= 합체 여부
    microbes = [list(map(int, input().split())) + [1] for _ in range(k)]

    microbe_moves(microbes, 0)
    result = 0
    for i in microbes:
        if i[-1] == 0:
            continue

        result += i[2]
    print(f'#{test_case} {result}')