MEMOIZATION = {}


def DFS(numbers, target, num_idx, equation):
    global MEMOIZATION

    equation = equation + str(numbers[num_idx])

    memorized_value = MEMOIZATION.get(f"{num_idx} {eval(equation)}", None)
    if memorized_value is not None:
        return memorized_value

    if num_idx == len(numbers) - 1:
        if eval(equation) == target:
            return 1
        else:
            return 0

    ret = 0
    for operator in ['+', '-']:
        new_equation = equation + operator
        DFS_ret = DFS(numbers, target, num_idx + 1, new_equation)
        ret = ret + DFS_ret

    MEMOIZATION[f"{num_idx} {eval(equation)}"] = ret

    return ret


def solution(numbers, target):
    answer = DFS(numbers, target, 0, "")
    answer = answer + DFS(numbers, target, 0, "-")

    return answer