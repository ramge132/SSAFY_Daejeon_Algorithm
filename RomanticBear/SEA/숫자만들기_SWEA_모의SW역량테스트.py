# 4008 숫자 만들기

# 1차 _ 완전탐색 _ 시간초과

'''
접근 방법 _ 완전 탐색 _ 시간초과 실패
: 연산자 리스트 -> 순열로 모든 경우의 리스트 -> 최대값 구해보기

문제점
- check_lst로 중복 순열을 계산하지 않음으로써 시간 복잡도를 줄이려 했으나 IF문은 시간 복잡도 영향 X 
  >> 연산자를 다쓰면 깊이 추가 되지 않는 방식으로 시간 복잡도를 줄이자 >> DFS 사용해야 함

'''
'''
# 피연산자 연산 함수
def caculater(num1, num2, operator):
    if operator == '+':
        ans = num1 + num2
    elif operator == '-':
        ans = num1 - num2
    elif operator == '*':
        ans = num1 * num2
    else:
        ans = int(num1 / num2) # 소수점 날림
    return ans


# 식 연산 함수
def sik_caculator(num_lst,operator_lst):
    ans=num_lst[0]
    for i in range(len(operator_lst)):
        num2=num_lst[i+1] # 피연산자 숫자
        ans=caculater(ans,num2,operator_lst[i])
    return ans


# 연산자 순열 생성, 중복 되지 않게 끔 check_lst에 담기
def perm(selected, remain):
    global check_lst

    if not remain:
        if selected not in check_lst:
            check_lst.append(selected)

    else:
        for i in range(len(remain)):
            select_i = remain[i]  # 남은 요소s
            remain_lst = remain[:i] + remain[i + 1:]
            perm(selected + [select_i], remain_lst)


# main문
T=int(input())
for tc in range(1,T+1):

    N=int(input())

    # 연산자 리스트
    # 임의 지정
    operator_num=list(map(int,input().split()))
    operator_lst=[]
    for i in range(len(operator_num)):
        if i==0:
            operator='+'
        elif i==1:
            operator='-'
        elif i==2:
            operator='*'
        else:
            operator='/'
        for _ in range(operator_num[i]):
            operator_lst.append(operator)


    # 피연산자 리스트
    num_lst=list(map(int,input().split()))

    # 연산자 중복 확인 리스트
    check_lst=[] 

    # 최댓값
    max_val=-1e8

    # 최솟값
    min_val=1e8
    perm([],operator_lst) # 피연산자 순열 생성 -> check_lst

    for oper in check_lst:
        ans=sik_caculator(num_lst,oper)
        # print('num_lst',num_lst)
        # print('oper',oper)
        # print(ans)
        if max_val<ans:
            max_val=ans
        if min_val>ans:
            min_val=ans

    print(f'#{tc}',max_val-min_val)

'''


# 2차 _ DFS _ 성공

'''
백트래킹(DFS)
- 연산자 카드가 남아있는 경우에 대해 모든 경우의 식을 만들어 처리 (단, 연산자 카드가 없으면 깊이 추가 불가)
- 연산 대상의 숫자: 배열 index 접근, 첫번째 원소: 첫번째 값 할당
- N(피연산자 길이)까지 돌면 max, min 값 갱신하고 종료

'''

# DFS 
def dfs(n,num,add,sub,mul,div):
    global max_val,min_val

    # DFS 종료조건
    # 마지막 인덱스(피연산자 끝)까지 돌면 최대값과 최소값 비교 후 갱신, 종료
    if n==N:
        min_val=min(min_val,num)
        max_val=max(max_val,num)
        return
    
    # DFS 분기조건
    # 개수가 0 이상인 연산자에 대해서만 DFS 수행
    if add>0:
        dfs(n+1,num+lst[n],add-1,sub,mul,div)
    if sub>0:
        dfs(n+1,num-lst[n],add,sub-1,mul,div)
    if mul>0:
        dfs(n+1,num*lst[n],add,sub,mul-1,div)    
    if div>0:
        dfs(n+1,int(num/lst[n]),add,sub,mul,div-1)


# main
T=10
for tc in range(1,T+1):
    N=int(input())

    add,sub,mul,div=map(int,input().split())
    lst=list(map(int,input().split()))

    min_val=int(1e8)
    max_val=int(-1e8)

    # num값 -> 피연산자 첫번째 값으로 초기화 / (피연산자 개수-1) -> 연산자 개수 : n값 1부터 시작
    dfs(1,lst[0],add,sub,mul,div)
    print(f'#{tc}',max_val-min_val)