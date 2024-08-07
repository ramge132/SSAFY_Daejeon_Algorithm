def password(l: list):
    target = 0
    while True:
        for i in range(1, 6):
            l[target] -= i
            if l[target] <= 0:
                l[target] = 0
                return l, target+1
            target += 1
            if target > len(l) - 1:
                target -= len(l)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t = int(input())
    input_list = list(map(int, input().split()))
    pwd_list, head = password(input_list)
    for _ in range(head):
        temp = pwd_list.pop(0)
        pwd_list.append(temp)
    pwd_list = list(map(str, pwd_list))
    print(f'#{t} {" ".join(pwd_list)}')
    # ///////////////////////////////////////////////////////////////////////////////////
