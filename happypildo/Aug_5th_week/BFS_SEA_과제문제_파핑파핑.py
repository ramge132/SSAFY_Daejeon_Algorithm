# disjoint로도 풀어보자
from collections import deque
from pprint import pprint

DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def look_around(N, game_map, i, j):
    ret = 0
    for dx, dy in DIRECTION:
        temp_i, temp_j = i + dx, j + dy
        if (-1 < temp_i < N) and (-1 < temp_j < N):
            if game_map[temp_i][temp_j] == '*': ret += 1
    return ret


def reveal_all_number(N, game_map):
    revealed_map = [[0 for j in range(N)] for i in range(N)]
    
    non_zero_location = set()
    zero_location = set()
    for i in range(N):
        for j in range(N):
            if game_map[i][j] == '*': revealed_map[i][j] = '*'
            else:
                ret = look_around(N, game_map, i, j)
                if ret != 0: non_zero_location.add((i, j))
                else: zero_location.add((i, j))
                revealed_map[i][j] = str(ret)
                
    return revealed_map, zero_location, non_zero_location


def cnt_zero_island(revealed_map, zero_location):
    is_visited = set()
    queue = deque()

    ret = 0
    non_zero_location = set()
    for init_point in zero_location:
        if init_point not in is_visited:
            ret += 1

            is_visited.add(init_point)
            queue.append(init_point)

            while queue:
                x, y = queue.popleft()

                for dx, dy in DIRECTION:
                    temp_x, temp_y = x + dx, y + dy
                    if (-1 < temp_x < N) and (-1 < temp_y < N):
                        if revealed_map[temp_x][temp_y] == "0" and (temp_x, temp_y) not in is_visited:
                            is_visited.add((temp_x, temp_y))
                            queue.append((temp_x, temp_y))
                        elif revealed_map[temp_x][temp_y].isdigit() and revealed_map[temp_x][temp_y] != "0":
                            non_zero_location.add((temp_x, temp_y))

    return ret, non_zero_location


def solve(N, game_map):
    revealed_map, zero_location, non_zero_location = reveal_all_number(N, game_map)
    non_zero_cnt, non_zero_location_trimmed = cnt_zero_island(revealed_map, zero_location)
    ans = non_zero_cnt + len(non_zero_location - non_zero_location_trimmed)

    return ans

T = int(input())

for t_iter in range(1, T+1):
    N = int(input())

    game_map = []
    for n_iter in range(N):
        game_map.append(input())

    print(f"#{t_iter} {solve(N, game_map)}")