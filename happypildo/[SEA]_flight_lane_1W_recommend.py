def check_validity(lane, idx, X, slope_location):
    # 1. 올라가는 경사 확인
    if idx + X < len(lane):
        target_h = lane[idx+X]
        if lane[idx:idx+X] == [target_h-1] * X and 1 not in slope_location[idx:idx+X]:
            for i in range(idx, idx+X):
                slope_location[i] = 1
            return X, True

    # 2. 내려가는 경사 확인
    if idx + X < len(lane):
        target_h = lane[idx]
        if lane[idx+1:idx+1+X] == [target_h-1] * X and 1 not in slope_location[idx+1:idx+1+X]:
            for i in range(idx+1, idx+1+X):
                slope_location[i] = 1
            return X, True

    # 3. 둘 다 못 할 경우, 평지가 이어질 수 있고 아닐 수도 있다.
    if idx == len(lane) - 1:           # 마지막 인덱스였다면, 앞에서 True였을테니 True 반환
        return 1, True
    elif lane[idx] == lane[idx+1]:     # 다음과 같다면, 평지가 이어질 수 있다. 일단 True 반환
        return 1, True
    else:                              # 갑자기 높이가 높아지거나/낮아지는 경우 밖에 없음 -> False 반환 -> 다음 lane으로 이동
        return 0, False

T = int(input())
result_line = ""
for t_iter in range(1, T+1):
    N, X = list(map(int, input().split()))

    flight_lane = []
    for _ in range(N):
        flight_lane.append(list(map(int, input().split())))

    lane_count = 0
    for i in range(N):
        new_line = flight_lane[i]
        slope_location = [0 for _ in range(len(new_line))]
        j = 0

        while j < len(new_line):
            offset, is_valid = check_validity(new_line, j, X, slope_location)

            if is_valid:
                j = j + offset
            else:
                break

            if j > len(new_line) - 1:
                lane_count = lane_count + 1

    for i in range(N):
        new_line = [flight_lane[j][i] for j in range(len(flight_lane))]
        slope_location = [0 for _ in range(len(new_line))]
        j = 0

        while j < len(new_line):
            offset, is_valid = check_validity(new_line, j, X, slope_location)

            if is_valid:
                j = j + offset
            else:
                break

            if j > len(new_line) - 1:
                lane_count = lane_count + 1

    print(f"#{t_iter} {lane_count}")

