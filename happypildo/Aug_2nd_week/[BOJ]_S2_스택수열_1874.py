N = int(input())

stack = []
operations = ""

can_make = True
push_start_number = 0
for n_iter in range(N):
    target_number = int(input())
    
    # stack의 헤드
    for i in range(push_start_number+1, target_number + 1):
        stack.append(i)
        operations += "+\n"

    # 스택에서 하나 씩 빼보면서, target_number와 같은지 비교
    while True:
        if len(stack) == 0:
            can_make = False
            break
        item = stack.pop()
        operations += "-\n"

        if item == target_number:
            break
    
    # push_start_number 갱신
    if push_start_number < target_number:
        push_start_number = target_number
    if not can_make:
        break

if can_make:
    print(operations)
else:
    print("NO")