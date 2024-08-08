# O(N) 풀이법

N = list(map(int,input().split()))
K = len(N)

result = 0

# 이중 for문을 사용하면 O(N**2)이 된다.
# a + b = 100 이기 때문에 a b 둘다 찾아야 된다.
# 리스트에서 숫자 a를 출력한 후 b = 100 - a 를 이용해서 b를 추출
# 추출한 b가 리스트에 존재하는지 확인한다.
# 확인하는 과정은 O(1)을 가진다.

for i in N:
    j = 100 - i
    if j in N:
        result = 1

print(result)





'''
# O(N**2) 풀이법
N = list(map(int,input().split()))

K = int(input())

result = 0

for i in range(K):
    # 2개의 원소를 더해야 하기 때문에 하나씩 올라가야 된다.
    for j in range(i):
        if N[i] + N[j] == 100:
            result = 1
            break

print(result)

# 시간 복잡도는 O(N^2)'''