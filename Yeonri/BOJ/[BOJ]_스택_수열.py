N = int(input())

lst = []
result = []
result_str = []

i = 1
cnt = 0

# 수열을 리스트에 저장한 후, 같은 숫자가 존재할 때, pop을 이용해서 뺀다.
# 이때, 사라진 값의 자리를 채우기 위해 저장된 수들을 전부 이동시켜야 한다. O(N)
# 수열을 저장한 리스트를 반전시켜 pop을 하여도 리스트를 전부 이동시키지 않아도 된다.
# 하지만 끝까지 탐색을 해야 하므로, O(N)이다.

for _ in range(N):
    lst.append(int(input().strip()))

while cnt < N*2:

    if len(result) > 0 and lst[0] == result[-1]:
        lst.pop(0)
        result.pop(-1)
        result_str.append('-')
        cnt += 1

    else:
        result.append(i)
        result_str.append('+')
        i += 1
        cnt += 1

if len(result) != 0:
    print('NO')
else:
    for i in range(len(result_str)):
        print(result_str[i])

print(dict)