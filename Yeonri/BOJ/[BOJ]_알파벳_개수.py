lst = list(input().strip())

# ord('문자')
# 하나의 chr 문자를 받고 유니코드 정수를 반환한다.
# chr(유니코드 정수)를 사용하면 문자열로 반환한다.

# 리스트에 알파벳 전부 넣는 방법
# alpha_lst = [chr(i) for i in range(ord('a'), ord('z')+1)]

# 딕셔너리에 알파벳 전부 넣는 방법
alpha_dic = {chr(i) : 0 for i in range(ord('a'), ord('z')+1)} # O(N)

for i in lst: #O(N)
    alpha_dic[i] += 1

# print(alpha_dic.values())
# dict_values([1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# string 모듈을 이용해서 가져올 수도 있다.
# import string
# alpha_dic = {char: 0 for char in string.ascii_lowercase}

for values in alpha_dic.values():
    print(values, end = ' ')
# end = ' '를 사용하면 출력값 뒤에 ' '를 붙인 후, 이어서 출력하게 된다.