from itertools import combinations

def check_stability(film, D, W, K):
    for w_iter in range(W):
        # run이 있는지 확인해보자.
        prev_char = film[0][w_iter]
        run_length = 1
        is_stable = False
        for d_iter in range(D):
            if prev_char == film[d_iter][w_iter]:
                run_length += 1
                if run_length > K:
                    # go to next width
                    is_stable = True
                    break
            else:
                run_length = 2
            prev_char = film[d_iter][w_iter]
        if not is_stable:
            return False
    return True


judgement = False
def recursively_check(film, D, W, K, inject_comb, depth):
    global judgement
    if depth == len(inject_comb):
        if check_stability(film, D, W, K):
            judgement = True
        else:
            return
    if judgement:
        return

    layer = inject_comb[depth]

    for type in range(2):
        temp_film = [f[:] for f in film]
        temp_film[layer] = [type for _ in range(W)]
        recursively_check(temp_film, D, W, K, inject_comb, depth+1)


def solve(film, D, W, K):
    global judgement
    judgement = False

    for k_iter in range(0, D + 1):
        for comb in combinations([d for d in range(D)], k_iter):
            recursively_check(film, D, W, K, comb, 0)
            if judgement:
                return k_iter

    return -1

T = int(input())
for t_iter in range(1, T+1):
    D, W, K = list(map(int, input().split()))

    input_film = [list(map(int, input().split())) for d_iter in range(D)]

    result = solve(input_film, D, W, K)

    print(f"#{t_iter} {result}")