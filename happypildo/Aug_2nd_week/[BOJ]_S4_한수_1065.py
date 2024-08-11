"""
# 문제 설명
- "한수"의 정의는 어떤 양의 정수 X의 각 자릿수가 등차수열을 이룰 때 X를 한수라 한다.
- N이 주어졌을 때, 1보다 크거나 같고 N보다 작거나 같은 한수의 개수를 출력하라.

# 접근 방법
- N보다 작은 한수를 하나씩 만들어 가면서 숫자를 카운트 했습니다.
"""
def count_number_of_perms(current_str, step_size, N):
    if int(current_str) > N:
        return 0
    
    ret = 1

    new = str(int(current_str[-1]) + step_size)
    if int(new) > 9:
        return ret
    elif int(new) < 0:
        return ret
    else:
        return ret + count_number_of_perms(current_str+new, step_size, N)

N = int(input())
answer = 9
if N < 10:
    answer = answer - (9 - N)
for i in range(1, 10):
    for step in range(0, 9):
        if i + step < 10:
            answer += count_number_of_perms(str(i) + str(i+step), step, N)

    for step in range(-9, 0):
        if i + step > -1:
            answer += count_number_of_perms(str(i) + str(i+step), step, N)
    
print(answer)