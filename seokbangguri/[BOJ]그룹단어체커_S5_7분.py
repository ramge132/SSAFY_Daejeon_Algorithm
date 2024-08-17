
# 시작 09:30 종료 09:37

T = int(input())

answer = 0
for test_case in range(1, T + 1):
    word = list(input())
    last_s = ''
    result_set = set()
    
    is_group = True
    for s in word:
        length = len(result_set)
        result_set.add(s)
        if last_s != s and length == len(result_set):
            is_group = False
            break
        last_s = s
    
    if is_group:
        answer += 1

print(answer)