# import sys
# sys.stdin = open('활주로건설.txt', 'r')

def build(lst):
    global total
    result = 0

    cnt = 1
    flag = True
    down = False

    # 스터디 피드백을 통해 elif를 이용한 조건문들 대신 else를 이용해서 필요 없는 구문들을 제거

    # 1. 활주로 길이 검사 X를 X-1과 혼합하여 사용하지 않도록 기본 cnt값을 1로 설정하였습니다.

    # 2. elif abs(lst[i] - lst[i + 1]) > 0: 구문을 통한 높이 차이 접근을 제거하였습니다.

    # 3. abs(lst[i] - lst[i + 1]) > 1를 else로 처리하였습니다.

    # 4. 각 문장에서 만들 수 없을 경우 > else를 이용해서 flag = False break 를 설정하였습니다.

    # 5. result를 저장할 필요가 없으므로 삭제하였으며, 조건에 만족하지 않으면 바로 break를 하도록 설정하였습니다.

    # 이를 통해 211122와 같이 서로 겹쳐서 활주로를 생성하는 문제를 elif를 통해 하나씩 처리할 수 있도록 만들었습니다.
    # 이전 코드는 if를 사용해서 중복으로 탐색할 수 있도록 만들었습니다.
    # 이유는 만약 현재 위치와 다음 위치의 높이가 같을 때, 즉각적으로 활주로 설치 유무를 확인하기 위함이었습니다.

    for i in range(N - 1):

        # 같을 때,
        if lst[i] == lst[i + 1]:
            cnt += 1

            if down == True and cnt == X:  # 내려가는 활주로를 만들 수 있을 때,
                cnt = 0
                down = False

        elif lst[i] + 1 == lst[i + 1]:
            if down == False and cnt >= X:  # down = False and 올라가는 활주로를 만들 수 있을 때
                cnt = 1
            else:
                flag = False
                break

        elif lst[i] - 1 == lst[i + 1]:  # 다음 지형이 1 낮은 높이
                if down == False:  # 내려가는 활주로가 만들어 지지 않고 있을 때,
                    down = True
                    cnt = 1

                else:  # 내려가는 활주로가 만들어지고 있는 중인데 낮아질 때,
                    flag = False
                    break

        else:
            flag = False
            break

    if down:
        flag = False

    if flag == True:
        total += 1


T = int(input())

for test_case in range(1, T + 1):
    N, X = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]

    total = 0  # 활주로를 만들 수 있는 총 개수

    for row in range(N):
        build(lst[row])

    for j in range(N):
        col = [lst[i][j] for i in range(N)]
        build(col)

    print(f'#{test_case} {total}')

    # 높이가 다를 때,
'''        elif abs(lst[i] - lst[i + 1]) > 0:

            if lst[i] + 1 == lst[i + 1]:  # 1 높은 지형일 때,

                if down == False and cnt >= X - 1:  # down = False and 올라가는 활주로를 만들 수 있을 때
                    result += 1
                    cnt = 0

                else:  # 만들 수 없으므로, break
                    flag = False
                    break

            if lst[i] - 1 == lst[i + 1]:  # 다음 지형이 1 낮은 높이

                if down == False:  # 내려가는 활주로가 만들어 지지 않고 있을 때,
                    down = True
                    cnt = 1


                elif down == True:  # 내려가는 활주로가 만들어지고 있는 중인데 낮아질 때,
                    flag = False
                    break

            if abs(lst[i] - lst[i + 1]) > 1: # 지형의 높낮이가 1 차이가 아닐 때,
                flag = False
                break

        if cnt == N-1: # 지형의 크기가 일정한 경우
            result += 1

    # if test_case == 4:
    #     print(' ')
    #     print(flag)
    #     print(result)
    #     print('=====')

    # 내려가는 활주로를 만드는 중에 끝났으면 false
    if down == True:
        result = 0
        flag = False

    if flag == True:
        if result > 0:
            total += 1
        return
    else:
        return'''


'''def build(lst):
    flag = True
    down = False
    result = 0
    cnt = 0

    # 만들고 큰 수가 나와야됨
    for i in range(N-1):

        # 같을 때,
        if lst[i] == lst[i+1]:
            cnt += 1
            # 시작 부분
            if i == 0:
                cnt += 1
            # 끝 부분
            if i + 1 == N + 1:
                cnt += 1

            # 내려가는 것 // 끝
            if down == True and cnt == X + 1:
                result += 1
                down = False
            continue



        # 차이가 존재할 때,
        if abs(lst[i] - lst[i+1]) != 0:

            # 올라가는 것 // 끝 // 성공
            if cnt <= X + 1 and lst[i] + 1 == lst[i + 1]:
                cnt = 0
                result += 1
                continue

            # 내려가는 것 // 시작
            if lst[i] -1 == lst[i + 1]:
                down = True
                cnt = 0
                cnt += 1
                continue

            # 높이 차이가 2 가 존재할 때, flag False break
            if abs(lst[i] - lst[i + 1]) >= 2:
                flag = False
                break

            # 카운트를 전부 채워서 활주로를 설정 못했는데, 올라가는 턱이 존재하는 경우
            if lst[i] + 1 == lst[i + 1] and cnt <= X:
                flag = False
                break

            # 활주로를 생성하고 있는데, 아래로 내려가는 경우
            if lst[i] - 1 == lst[i + 1] and cnt <= X:
                down = False
                flag = False
                break

    if flag == True:
        return result
    else:
        return 0'''


'''def build(idx, total):
    line = lst[idx]
    max_depht = max(line)

    total = 0

    # 끝에 존재할 때,
    for i in range(len(line) - X + 1):
        if line[i] == max_depht: continue
        count = 1

        # 시작 부분
        if i == 0:
            for j in range(i + 1, i + X):
                if line[i] == line[j]:
                    count += 1

                    if i == i + X - 1 and count == X and line[i] + 1 == line[j]:
                        total += 1

                if line[i] != line[j]:
                    count = 1

        # 끝부분 -> 바로 전 값이 현재 값보다 1 클때,
        if i == len(line) - X and line[i - 1] == line[i] + 1:
            for j in range(i + 1, i + X - 1):
                if line[i] == line[j]:
                    count += 1

                    if i == i + X - 1 and count == X and line[i] + 1 == line[j]:
                        total += 1

                if line[i] != line[j]:
                    count = 0

    print(total)

        # else:
        #     for j in range(i,i + X + 1):
        #         if line[i] == line[j]:
        #             count += 1
        #         else:
        #             count = 0
        #         if count == X + 1:
        #             total += 1

    # for i in range(len(line) - X - 1):
    #     if line[i] == max_depht: continue
    #     count = 0
    #     for j in range(i,i + X + 1):
    #         if line[i] == line[j]:
    #             count += 1
    #         else:
    #             count = 0
    #         if count == X + 1:
    #             total += 1

    print(total)


    # 활주로 건설 가능 라인 확인
    # dict를 이용해서 개수를 저장한다.
    # 저장된 개수를 이용해서 건설할 수 있는지 먼저 확인
    # if len(chk_dic) > 0:
    #     for i in chk_dic.keys():
    #         if chk_dic[i] > X:
    #             print(chk_dic[i])
    #             total += 1
    #             return
        



for test_case in range(1, T + 1):
    N, X = map(int, input().split())

    lst = [list(map(int,input().split())) for _ in range(N)]

    build(0, 0)
    # 경사로 생성
    # 배열의 맨 끝 0, N-1에는 다음 번에 높이가 같은 값이 존재하지 않아도 된다.
    # 22233으로 되어 있을 때, 맨 앞에 같은 높이의 2가 존재해서 설치할 수 있다.
    # 332211 경사로를 설치할 수 있다.

    # 1. 경사로의 시작 부분이 배열의 끝에 존재하면 가능
    # 2. 경사로 다음에 같은 높이의 수가 존재할 때, 가능

    # 제일 높은 값을 찾아서  그보다 작은 값을 count해서 x만큼 존재하는지 확인
    # 활주로의 시작 - 1 끝 + 1 을 하여 양옆의 값 확인, 한쪽은 높고, 한쪽은 같아야함
    #
    # 활주로를 건설할 크기 x만큼 같은 높이의 값이 연속해서 존재할 경우
    #
'''