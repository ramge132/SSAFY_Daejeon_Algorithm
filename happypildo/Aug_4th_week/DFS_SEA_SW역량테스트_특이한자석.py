def rotate_magnetic(magnetic, direction):
    temp_magnetic = None
    if direction == 1:
        temp_magnetic = [magnetic[-1]] + magnetic[:-1]
    elif direction == -1:
        temp_magnetic = magnetic[1:] + [magnetic[0]]
    return temp_magnetic


def recursive_rotate(magnetics, is_left, target_magnetic, original_magentic, original_direction):
    if is_left and target_magnetic == 0:
        return
    if not is_left and target_magnetic == 5:
        return

    first, second = 2, 6
    offset = -1
    if not is_left: 
        first, second = second, first
        offset *= -1

    have_to = False
    if is_left and target_magnetic - 1 > 0: 
        if magnetics[target_magnetic - 2][first] != magnetics[target_magnetic - 1][second]:
            have_to = True
    elif not is_left and target_magnetic + 1 < 5: 
        if magnetics[target_magnetic][first] != magnetics[target_magnetic - 1][second]:
            have_to = True
    
    magnetics[target_magnetic - 1] = rotate_magnetic(magnetics[target_magnetic - 1], original_direction * -1)

    if have_to:
        recursive_rotate(magnetics, is_left, target_magnetic+offset, target_magnetic, original_direction * -1)


def solve(magnetics, rotate_order):
    for idx, direction in rotate_order:
        have_to_left = False
        have_to_right = False
        if idx - 1 > 0:
            if magnetics[idx - 2][2] != magnetics[idx - 1][6]:
                have_to_left = True
        if idx + 1 < 5:
            if magnetics[idx][6] != magnetics[idx - 1][2]:
                have_to_right = True

        magnetics[idx - 1] = rotate_magnetic(magnetic=magnetics[idx - 1], direction=direction)
        if have_to_left: recursive_rotate(magnetics, True, idx - 1, idx, direction)
        if have_to_right: recursive_rotate(magnetics, False, idx + 1, idx, direction)


T = int(input())
for t_iter in range(1, T+1):
    K = int(input())

    magnetics = [list(map(int, input().split())) for _ in range(4)]
    magnetics = magnetics
    rotate_order = [list(map(int, input().split())) for _ in range(K)]

    solve(magnetics, rotate_order)

    total_score = 0
    for idx in range(4):
        if magnetics[idx][0] == 1:
            total_score = total_score + 2 ** idx

    print(f"#{t_iter} {total_score}")
