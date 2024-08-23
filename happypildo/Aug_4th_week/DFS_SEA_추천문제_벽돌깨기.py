from collections import deque

orders = set()
def make_order(N, W, selected):
    global orders
    
    if len(selected) == N:
        orders.add(tuple(selected))
        return

    for w in W:
        make_order(N, W, selected + [w])


def bomb(brick_map, H, W, to_bomb, is_bombed):
    while to_bomb:
        loc = to_bomb.popleft()

        if loc in is_bombed:
            continue
        else:
            is_bombed.add(loc)

            x, y = loc[0], loc[1]
            bomb_range = brick_map[x][y]
            ranges = [i for i in range(-1 * (bomb_range - 1), bomb_range)]
            for offset in ranges:
                if ((x+offset, y) not in is_bombed) and (-1 < x+offset < H) and brick_map[x+offset][y] != 0:
                    to_bomb.append((x+offset, y))
                if (x, y+offset) not in is_bombed and (-1 < y+offset < W) and brick_map[x][y+offset] != 0:
                    to_bomb.append((x, y+offset))
    
    return is_bombed


def find_target(brick_map, x, y, H):
    while -1 < x < H:
        if brick_map[x][y] != 0:
            return (x, y)
        x += 1
    return -1


def arrange_brick_map(brick_map, H, W, is_bombed):
    for bombed_x, bombed_y in is_bombed:
        brick_map[bombed_x][bombed_y] = 0
    for y in range(W):
        temp_line = []
        for x in range(H - 1, -1, -1):
            if brick_map[x][y] != 0:
                temp_line.append(brick_map[x][y])
        while len(temp_line) != H:
            temp_line.append(0)

        for idx, x in enumerate(range(H - 1, -1, -1)):
            brick_map[x][y] = temp_line[idx]

    return brick_map


def solve(input_map, N, W, H, num_of_bricks):
    global orders
    orders = set()
    make_order(N, [i for i in range(W)], [])
    
    min_remain = float('inf')
    for order in orders:
        temp_brick_map = [input_map[h][:] for h in range(H)]
        for y in order:
            target = find_target(temp_brick_map, 0, y, H)
            
            if target == -1:
                break
            
            is_bombed = set()
            to_bomb = deque([target])
            new_is_bombed = bomb(temp_brick_map, H, W, to_bomb, is_bombed)
            temp_brick_map = arrange_brick_map(temp_brick_map, H, W, new_is_bombed)

        cnt = 0
        for x in range(H):
            for y in range(W):
                if temp_brick_map[x][y] != 0:
                    cnt += 1
        
        if min_remain > cnt:
            min_remain = cnt
        if min_remain == 0:
            return 0
    return min_remain


T = int(input())
for t_iter in range(1, T+1):
    N, W, H = list(map(int, input().split()))

    input_map = []
    num_of_bricks = 0
    for h in range(H):
        input_list = list(map(int, input().split()))
        for val in input_list:
            if val != 0: num_of_bricks += 1
        input_map.append(input_list)

    answer = solve(input_map, N, W, H, num_of_bricks)

    print(f"#{t_iter} {answer}")