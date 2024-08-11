N = int(input())

lst = [False] * 2000001
result = []

# 리스트에 먼저 문제에서 주어진 최대 크기만큼 False를 설정한다.
# 숫자들이 들어오면 False를 True로 변경을 한다.
# True값을 가진 인덱스만 출력하도록 만든다.

# 문제에서 입력된 수는 절대값이 10000000보다 작거나 같은 정수라고 하였으므로,
# - 값을 생각해야 한다.
# 인덱스에 - 값은 존재하지 않기 때문에 정수로 만들어 준다.
# 따라서 - 값은 1000000을 더해준 것으로 표현을 하고,
# result에 추가를 할 때, 1000000을 빼준다.

for _ in range(N):
    num = int(input())
    lst[num + 1000000] = True

for i in range(len(lst)):
    if lst[i] == True:
        result.append(i - 1000000)

for i in result:
    print(i)

