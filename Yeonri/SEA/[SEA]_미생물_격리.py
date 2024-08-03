import sys
sys.stdin = open('미생물격리.txt', 'r')

# 상 하 좌 우
DXY = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

def turn(idx):
    if idx == 1:
        return 2
    if idx == 2:
        return 1
    if idx == 3:
        return 4
    if idx == 4:
        return 3

T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    microb_dict = {}
    count = 0
    total = 0

    for _ in range(K): # 미생물의 개수 만큼
        x, y, num, dir = map(int, input().split())
        microb_dict.setdefault((x, y), []).append((num, dir))

    while count < M:
        count += 1
        tmp_dict = {}

        for (x, y), microb_lst in microb_dict.items():

            # microb에 존재하는 미생물들의 개수를 비교
            # 군집이 더 큰 쪽의 이동으로 변경한다.
            max_num = 0
            max_dir = 0

            # 방향을 바꿀 필요 없이 제일 큰 값만 찾아서 더해주면 된다.
            for num, dir in microb_lst:
                if num > max_num:
                    max_num = num
                    max_dir = dir

            total_num = sum(microb[0] for microb in microb_lst)
            dx, dy = DXY[max_dir]
            nx, ny = x + dx, y + dy

            if 0 == nx or N - 1 == nx or 0 == ny or N - 1 == ny:
                total_num //= 2
                max_dir = turn(max_dir)


            tmp_dict.setdefault((nx, ny), []).append((total_num, max_dir))

        microb_dict = tmp_dict

    total = sum(microb[0] for group in microb_dict.values() for microb in group)

    # for (x, y), microb_lst in microb_dict:
    #     for microb in microb_lst:
    #         e, dir = microb
    #         total += e

    print(f'#{test_case} {total}')