DIRECTION = [
    [+1, -1], [+1, +1], [-1, +1], [-1, -1]
]   # 좌하 / 우하 / 우상 / 좌상
 
 
largest_dessert = -1
def recursively_solve(N, cafe_map, start_pos, ate_dessert, cur_dir, cur_pos, moving_info):
    global largest_dessert
    
    if cur_dir == 2 and moving_info[2] == 0:
        if len(ate_dessert) * 2 < largest_dessert:
            return
    if cur_dir > 0 and len(ate_dessert) == 1:
        return
    if (cur_pos[0] - 1 == start_pos[0] and cur_pos[1] - 1 == start_pos[1]) and len(ate_dessert) != 1:
        if largest_dessert < len(ate_dessert):
            largest_dessert = len(ate_dessert)
        return
    if cur_dir > len(DIRECTION) - 1:
        # 네 방향 갔지만, 원점에 도착하지 못한 경우
        return
     
    x, y = cur_pos
    temp_x, temp_y = x + DIRECTION[cur_dir][0], y + DIRECTION[cur_dir][1]
 
    if (-1 < temp_x < N) and (-1 < temp_y < N):
        target_dessert = cafe_map[temp_x][temp_y]
        if target_dessert not in ate_dessert:
            # 약속된 방향으로 계속 이동
            temp_moving1 = moving_info[:]
            temp_moving1[cur_dir] += 1
            recursively_solve(N, cafe_map, start_pos, 
                              ate_dessert | set([target_dessert]), cur_dir, (temp_x, temp_y), temp_moving1)
            
            temp_moving2 = moving_info[:]
            temp_moving2[cur_dir] += 1
            recursively_solve(N, cafe_map, start_pos, 
                              ate_dessert | set([target_dessert]), cur_dir + 1, (temp_x, temp_y), temp_moving2)
        else:
            # 한 단계 나아가기
            recursively_solve(N, cafe_map, start_pos, 
                              ate_dessert, cur_dir + 1, cur_pos, moving_info)
    else:
        recursively_solve(N, cafe_map, start_pos, 
                              ate_dessert, cur_dir + 1, cur_pos, moving_info)
 
def solve(N, cafe_map):
    global largest_dessert
    largest_dessert = -1
    for i in range(N):
        for j in range(N):
            ate_dessert = set([cafe_map[i][j]])
            recursively_solve(N, cafe_map, (i, j), ate_dessert, 0, (i, j), [0, 0, 0, 0])
 
 
T = int(input())
for t_iter in range(1, T+1):
    N = int(input())
 
    cafe_map = [list(map(int, input().split())) for n_iter in range(N)]
     
    solve(N, cafe_map)
 
    answer = largest_dessert
    print(f"#{t_iter} {answer}")