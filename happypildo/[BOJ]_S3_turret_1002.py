T = int(input())

for t_iter in range(1, T+1):
    x_a, y_a, r_a, x_b, y_b, r_b = list(map(float, input().split()))

    if r_a < r_b:
        temp = [x_b, y_b, r_b]
        x_b, y_b, r_b = x_a, y_a, r_a
        x_a, y_a, r_a = temp

    distance = (x_a - x_b) ** 2 + (y_a - y_b) ** 2
    distance = distance ** 0.5

    answer = -1

    if x_a == x_b and y_a == y_b and r_a == r_b:
        answer = -1
    elif distance < r_a:
        if r_b < r_a - distance:
            answer = 0
        elif r_b > r_a - distance:
            answer = 2
        else:
            answer = 1
    elif distance > r_a:
        if r_b < distance - r_a:
            answer = 0
        elif r_b > distance - r_a:
            answer = 2
        else:
            answer = 1
    elif distance == r_a:
        answer = 2

    print(answer)


