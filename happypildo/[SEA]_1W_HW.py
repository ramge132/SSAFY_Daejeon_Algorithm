OPERATORS = ['+', '-', '*', '/']
OPERATOR_ORDERS = []
memoization = {}


def recursively_make_operator_order(selected, remain):
    global OPERATOR_ORDERS
    global memoization

    if memoization.get(selected, 0) == remain:
        return
    if remain == "":
        OPERATOR_ORDERS.append(selected)
    for idx in range(len(remain)):
        memoization[selected] = remain
        recursively_make_operator_order(selected + remain[idx], remain[:idx] + remain[idx + 1:])


def get_possible_calculation(num_set):
    global OPERATOR_ORDERS
    possible_calculation = []

    for operator_order in OPERATOR_ORDERS:
        temp_num_set = num_set[:]
        result = 0

        for offset in range(0, len(num_set) - 1):
            left_hand = temp_num_set[offset]
            right_hand = temp_num_set[offset + 1]
            operator = operator_order[offset]

            if operator == '+':
                result = left_hand + right_hand
            elif operator == '-':
                result = left_hand - right_hand
            elif operator == '*':
                result = left_hand * right_hand
            elif operator == '/':
                result = int(left_hand / right_hand)

            temp_num_set[offset + 1] = result

        possible_calculation.append(result)

    return possible_calculation


T = int(input())
for t_iter in range(1, T + 1):
    N = int(input())
    operator_count_set = [n for n in list(map(int, input().split()))]
    num_set = [n for n in list(map(int, input().split()))]

    operator_set = ""
    for idx, count in enumerate(operator_count_set):
        for _ in range(count):
            operator_set = operator_set + OPERATORS[idx]

    OPERATOR_ORDERS = []
    memoization = {}

    recursively_make_operator_order("", operator_set)
    results = get_possible_calculation(num_set)
    print(f"#{t_iter} {max(results) - min(results)}")
