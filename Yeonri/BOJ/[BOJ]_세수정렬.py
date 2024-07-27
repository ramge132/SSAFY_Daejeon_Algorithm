lst = list(map(int,input().split()))

# max(lst), min(lst)
# sorted

# count_sort 사용

mx = max(lst)

count_lst = [0] * (mx+1)
count_sort = []

for i in lst:
    count_lst[i] += 1

# 값이 1 이상인 리스트의 인덱스 값만 추출하여 count_sort 리스트에 저장
for i in range(len(count_lst)):
    if count_lst[i] > 0:
        # for _ in count_lst[i]:
        #     count_sort.append(i)
        count_sort.extend([i] * count_lst[i])

for i in count_sort:
    print(i, end=' ')


# 버블 정렬
# for i in range(len(lst)-1):
#     for j in range(i+1,len(lst)):
#         if lst[i] > lst[j]:
#             # lst[i],lst[j] = lst[j],lst[i]

#             tmp = lst[i]
#             lst[i] = lst[j]
#             lst[j] = tmp

# for i in lst:
#     print(i,end=' ')


'''
if mx[0] > lst[i]:

    tmp = mx[0]
    # mx에 lst[i]값 
    mx[0] = lst[i]

    lst[mx[1]] = lst[i]

    lst[i] = tmp

    mx[1] = i
'''


'''5 2 7

mx에 5 0

tmp에 5 저장

mx에 lst[i] 값을 저장

lst[i] 값을 lst[mx[0]]에 저장

mx[1] 에 i 저장

lst[i]에 tmp 저장'''