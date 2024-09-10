# 14501 퇴사

'''
dp풀이 1

- 해당 날짜와 이전 날짜들을 매번 비교
- 첫번째 날짜부터 접근

dp 테이블 갱신 조건
조건1: 현재 날짜에서 날짜를 추가했을 때(일을 한다면) 퇴사날 전까지 마무리 되어야 함   ... 현재 날짜에 대한 조건
조건2: 과거 날짜랑 비교할 때, 과거 날짜에서 날짜를 추가한 값이 현재날짜 이하여야 일이 가능함   ... 과거 날짜와 현재 날짜의 관계 조건


문제점 : for문 2회 사용

'''

N=int(input())

lst=[(0,0)] 
for _ in range(N):
    T,P=map(int,input().split())
    lst.append((T,P))

dp=[0]*(N+1)

for i in range(1,N+1):
    cur_t,cur_p=lst[i]

    for j in range(i):
        pre_t,pre_p=lst[j]

        # 현재 하려고 하는 일을 진행했을 때 마감기간이 아웃되지 않고, ㅁ
        if i+cur_t<=N+1:

            # 과거의 일을 진행했을 때, 겹쳐지지 않는다면 dp갱신
            if j+pre_t<=i:
                dp[i]=max(dp[i],dp[j]+cur_p)

print(max(dp))



'''
dp풀이 2

- dp테이블 end_day(i+cur_p)에 대해서 갱신 수행(과거와 비교할 필요 x)
- 현재 날짜에 대한 dp테이블 값만 초기화 (단, 다음날로 현재 날짜까지의 dp테이블 최고값을 넘겨주어야 함  >> 안넘겨 준다면 매번 dp테이블이 갱신됨)

'''

N=int(input())

lst=[(0,0)] 
for _ in range(N):
    T,P=map(int,input().split())
    lst.append((T,P))

dp=[0]*(N+2) # 인덱스 에러 회피 (dp[i+1] = max(dp[i+1],dp[i]))

for i in range(1,N+1):
    cur_t,cur_p=lst[i]

    end_day=i+cur_t

    # end_day에 해당되는 dp테이블 값과 현재에서 이득을 취했을 때 값 비교하여 더 높은 값으로 갱신
    if end_day<=N+1:
        dp[end_day]=max(dp[end_day],dp[i]+cur_p)

    if i+1<=N+1:
        # 현재까지의 최대 이익을 다음 날에 전달 (무조건, i+1<=end_day 만족)
        dp[i+1] = max(dp[i+1],dp[i])  

print(max(dp))



'''
dp풀이 3

- 뒤에서 부터 갱신
>> 선택하는 경우와 안하는 경우로 구분하여 더 큰 값으로 dp갱신 (이때, 일을 수행했을 때 날짜가 마감일 이하인지 확인해야함)  ... 약간 재귀호출이랑 dfs랑 비슷한 느낌임 
>> 이점 : 1중 for문 + 간단함 

'''

N=int(input())

lst=[] 
for _ in range(N):
    T,P=map(int,input().split())
    lst.append((T,P))

dp=[0]*(N+1)

for i in range(len(lst)-1,-1,-1):
    t,p=lst[i]

    if i+t>N:
        dp[i]=dp[i+1] # 선택 못함 = 다음 날짜 dp값 그대로 받아옴
    
    else:
        dp[i]=max(dp[i+1],dp[i+t]+p)  # dp[i+1]: 선택하지 않았을 때, dp[i+t]+t: 선택했을 때


print(dp[0])  # 뒤에서 부터 접근하면서 최댓값을 갱신 받아오기 때문에, 첫번째 인덱스에 최대값(max(dp))이 담기게 됨




'''
4. DFS 풀이

- 선택한 날과 선택하지 않은 날 완전탐색

'''

# idx -> 날짜, sm -> 현재까지 받아온 이득
def dfs(idx,sm):
    global ans

    # 퇴사일 초과 
    if idx>N:
        return 
    
    # 퇴사일이면
    if idx==N:
        ans=max(ans,sm)
        return
    
    # 마지막 날에서 최대이득이 아닐 수 있음
    ans=max(ans,sm)
    
    dfs(idx+lst[idx][0],sm+lst[idx][1])
    dfs(idx+1,sm)


N=int(input())

lst=[] 
for _ in range(N):
    T,P=map(int,input().split())
    lst.append((T,P))

ans=0
dfs(0,0)
print(ans)


'''
실행 속도: 1>2=3>4

'''