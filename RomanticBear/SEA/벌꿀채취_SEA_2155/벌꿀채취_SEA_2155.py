'''
내 생각

1. 
- 일단 M 길이 만큼의 모든 벌꿀 통 찾기

2. 
- C조건 이내 -> 그대로 두기
- C 초과 -> 일부 선택은 가능. 단, 이것도 C조건 따져야 함. 

3. 
- 순위 매겨서 2개 선택
- 안겹쳐지고 2개를 선택해야함 -> 조합(?) 

Q.
- 꿀통 겹쳐지지 않게 어떻게 뽑음 ,,? 
- 큰 값만 그리디하게 접근하면 정답이 아닌데 어떻게 접근해야함 ,,? 
>> 완탐 ? 

- 부분 채취할 때, C이하를 만족하는 최대값 어떻게 찾음 ,,?
>> DFS ?

'''

'''
풀이법

- 필기파일 첨부

1. 완탐으로 일꾼 두 명이 각각 선택할 수 있는 모든 경우의 수 따짐
2. 선택된 꿀 통에 대해서 DFS 수행하면서 C조건 따짐
3. 최대값 갱신해가며 정답 구하기

'''


# dfs
def dfs(n,Volume,sm,i,j):
    global max_val

    # 종료조건1: 용량 초과
    if Volume>C:
        return 

    # 종료조건2: 꿀통 내부 마지막칸(M) 초과     
    if n==M:
        max_val=max(max_val,sm)
        return  

    dfs(n+1,Volume,sm,i,j+1)    # 꿀 미포함 DFS호출
    dfs(n+1,Volume+lst[i][j],sm+lst[i][j]**2,i,j+1)  # 꿀 포함 DFS호출

# main
T=int(input())
for tc in range(1,T+1):
    N,M,C=map(int,input().split())
    lst=[list(map(int,input().split())) for _ in range(N)]
    ans=0

    # 일꾼1에서 위치와 일꾼2에서의 위치가 겹쳐지지 않기 때문에, DFS 최대값의 좌표 중복 안됨 -> 두 일꾼이 가질 수 있는 모든 조합 탐색 가능
    for i1 in range(N):
        for j1 in range(N-M+1):        
            max_val=0  # 꿀통 최대값
            dfs(0,0,0,i1,j1) 
            pf1=max_val # 일꾼1 최대값 갱신            
            for i2 in range(i1,N):
                sj=j1+M if i1==i2 else 0
                for j2 in range(sj,N-M+1):
                    max_val=0  # 꿀통 최대값                
                    dfs(0,0,0,i2,j2)
                    pf2=max_val  # 일꾼1 고른 최대값을 제외하고, 일꾼2가 고를 수 있는 최대값 갱신
                    ans=max(ans,pf1+pf2)  # 정답 갱신

    print(f'#{tc}',ans)



# memoization 방법
# 일꾼1 최댓값 구할 때, 이미 모든 좌표에서 DFS를 호출하였는데, 일꾼2 최댓값 구할 때 중복 호출하는 메모리 낭비문제 발생
# memoization 방법으로 각 좌표에서의 최댓값을 기록해두고, 일꾼1, 일꾼2 안겹쳐지게 완탐하면서 최댓값 구하자.

# dfs
def dfs(n,Volume,sm,i,j):
    global max_val

    # 종료조건1: 용량 초과
    if Volume>C:
        return 

    # 종료조건2: 꿀통 내부 마지막칸(M) 초과     
    if n==M:
        max_val=max(max_val,sm)
        return  

    dfs(n+1,Volume,sm,i,j+1)    # 꿀 미포함 DFS호출
    dfs(n+1,Volume+lst[i][j],sm+lst[i][j]**2,i,j+1)  # 꿀 포함 DFS호출


# main
T=int(input())
for tc in range(1,T+1):
    N,M,C=map(int,input().split())
    lst=[list(map(int,input().split())) for _ in range(N)]
    ans=0
    memo=[[0]*N for _ in range(N)]

    # MEMO 테이블 생성
    for i in range(N):
        for j in range(N-M+1):        
            max_val=0  # 꿀통 최대값
            dfs(0,0,0,i,j)
            memo[i][j]=max_val 

    # 두 조합의 최댓값 구하기
    for i1 in range(N):
        for j1 in range(N-M+1):          
            for i2 in range(i1,N):
                sj=j1+M if i1==i2 else 0
                for j2 in range(sj,N-M+1):
                    ans=max(ans,memo[i1][j1]+memo[i2][j2])  # 정답 갱신

    print(f'#{tc}',ans)