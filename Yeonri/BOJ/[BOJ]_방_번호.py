N = list(map(int,input().strip()))

# 플라스틱 번호 1세트를 딕셔너리에 설정
# enumerate를 이용해서 key에 for i in range(10) 까지의 수를 넣는다.

dic = {i:0 for i in range(10)}

for i in N:
    dic[i] += 1

# dic에 key 값이 6, 9를 제외한 숫자들이 2 이상일 때, 해당 숫자만큼 필요하다.
# 6, 9 >> 두 숫자의 합 // 2를 한다. 99
# 제일 높은 벨류가 정답이다.
#

def chk(n):
    global total
    if total < n:
        total = n

total = 0
number_count = 0
# 6699 -> 짝수일 때, 홀수일 때,

# for를 사용해서 하나씩 비교를 하는데
# 그냥 max를 사용해서 제일 큰 값을 찾은 후
# 6이랑 9 값만 탐색하면 되는거 아님?

# 6이랑 9 값이 존재할 때, 9가 없으면 6의 값이 제일 큰 값으로 들어간다.

for i in dic:
    if i == 6:
        number_count += dic[i]

    elif i == 9:
        number_count += dic[i]

    else:
        chk(dic[i])

if number_count % 2 == 0:
    num = number_count // 2
    chk(num)
else:
    chk(number_count // 2 + 1)

print(total)