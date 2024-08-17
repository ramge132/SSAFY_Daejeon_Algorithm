"""
# 문제 설명
- 여러 원(행성계 경계)의 좌표와 반지름이 주어진다. (이 때 원의 경계가 맞닿거나 교차하지 않는다.)
- 시작점과 도착점이 있을 때, 원의 범위를 최소한으로 지나면서 나가야 한다.
- 최소한의 경계를 드나드는 횟수는 몇인지 출력하시오.

# 해피필도 팁
- **원의 경계가 맞닿거나 교차하지 않는다.**라는 정보를 활용했을 때 발생하는 경우의 수를 생각해서 풀었습니다.
- if 문에서 xor 연산 `^`을 하고 싶다면, boolean 값이 비교될 수 있도록 괄호를 쳐야 합니다.
"""
def count_cross_line(start_point, end_point, star_information):
    stars_include_start = set()
    stars_include_end = set()

    for idx, star in enumerate(star_information):
        x_s, y_s, r_s = star
        distance_btw_start = (start_point[0] - x_s) ** 2 + (start_point[1] - y_s) ** 2
        distance_btw_start = distance_btw_start ** 0.5

        if distance_btw_start < r_s:
            stars_include_start.add(idx)

        distance_btw_end = (end_point[0] - x_s) ** 2 + (end_point[1] - y_s) ** 2
        distance_btw_end = distance_btw_end ** 0.5

        if distance_btw_end < r_s:
            stars_include_end.add(idx)

    cross_count = 0
    for idx in range(len(star_information)):
        if (idx in stars_include_start) ^ (idx in stars_include_end):
            cross_count += 1

    return cross_count

T = int(input())

for t_iter in range(T):
    start_x, start_y, end_x, end_y = list(map(int, input().split()))
    N = int(input())

    stars = [list(map(int, input().split())) for _ in range(N)]

    print(count_cross_line((start_x, start_y), (end_x, end_y), stars))