possible_combinations = []


def make_combinations(comb, remains, original_list, target_num):
    global possible_combinations

    if len(comb) == target_num:
        ret = [comb, [original_list[x] for x in range(len(original_list)) if x not in comb]]
        possible_combinations.append(ret)
        return

    for idx in range(len(remains)):
        make_combinations(comb + [remains[idx]], remains[idx+1:], original_list, target_num)


def search_best_combination(N, synergy_arr):
    min_gap = 987654321

    for ingredients_A, ingredients_B in possible_combinations:
        synergy_A = 0
        for first_idx, first_ingredient in enumerate(ingredients_A):
            for second_idx, second_ingredient in enumerate(ingredients_A[:first_idx] + ingredients_A[first_idx+1:]):
                synergy_A = synergy_A + synergy_arr[first_ingredient][second_ingredient]

        synergy_B = 0
        for first_idx, first_ingredient in enumerate(ingredients_B):
            for second_idx, second_ingredient in enumerate(ingredients_B[:first_idx] + ingredients_B[first_idx+1:]):
                synergy_B = synergy_B + synergy_arr[first_ingredient][second_ingredient]

        gap = abs(synergy_A - synergy_B)

        if gap < min_gap:
            min_gap = gap

    return min_gap


T = int(input())
for t_iter in range(1, T+1):
    N = int(input())

    synergy_arr = [list(map(int, input().split())) for _ in range(N)]

    possible_combinations = []
    make_combinations([], [x for x in range(N)], [x for x in range(N)], int(N/2))

    print(f"#{t_iter} {search_best_combination(N, synergy_arr)}")