import sys
N = int(sys.stdin.readline())

count = 0

lst = []
# 딕셔너리, set 순서가 없기 때문에 구현할 수 없다.
# 리스트로 구현

# input을 사용하면 시간 초과가 생긴다.
# sys.stdin.readline()을 사용해서 해결


for _ in range(N):
    command = list(sys.stdin.readline().split())
    if len(command) == 2:
        lst += [int(command[1])]

    else:
        if command[0] == 'pop':
            if len(lst) == 0:
                print(-1)
            else:
                print(lst.pop())
        elif command[0] == 'top':
            if len(lst) > 0:
                print(lst[-1])
            else:
                print(-1)

        elif command[0] == 'empty':
            if len(lst) > 0:
                print(0)
            else:
                print(1)

        elif command[0] == 'size':
            print(len(lst))
