def hanoi(N, start_poll, end_poll, middle_poll):
    result = ""

    if N == 1:
        return f"{start_poll} {end_poll}\n"

    result = result + hanoi(N-1, start_poll=start_poll, end_poll=middle_poll, middle_poll=end_poll)
    result = result + f"{start_poll} {end_poll}\n"
    result = result + hanoi(N-1, start_poll=middle_poll, end_poll=end_poll, middle_poll=start_poll)

    return result


N = int(input())

if N > 20:
    print(2 ** N - 1)
else:
    print(2 ** N - 1)
    print(hanoi(N=N, start_poll=1, end_poll=3, middle_poll=2))
