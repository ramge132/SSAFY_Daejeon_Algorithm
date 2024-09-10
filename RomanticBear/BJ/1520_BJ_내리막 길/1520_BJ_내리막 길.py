# 1520_BJ_내리막길

'''
풀이법

dfs

- 종료 조건: N-1,M-1 좌표 도착 >> CNT+1

- How to solve runtime error

>> dp
>> 해당 좌표에서 갈 수 있는 경로의 수를 dp 테이블에 저장 

///////////

Dynamic Programming => Memoization

비추 문제
- N으로 표현

추천 문제
- 2xN 타일링
- 피보나치 수열


'''

# 풀이노트 참고 

# DFS 
def dfs(i,j):
    global ans
    if DP[i][j] != -1: return DP[i][j]  # dp[N-1][M-1]에서 처음으로 1반환


    cur=lst[i][j]
    dij=[(-1,0),(1,0),(0,-1),(0,1)]

    roadCount = 0
    for di,dj in dij:
        ni,nj=i+di,j+dj

        if 0<=ni<N and 0<=nj<M:
            if lst[ni][nj]<cur:
                roadCount += dfs(ni,nj)

    DP[i][j] = roadCount        
    
    return DP[i][j]


# Main
N,M=map(int,input().split())
lst=[]

DP = [[-1 for _ in range(M)] for _ in range(N)]
DP[N-1][M-1] = 1

for _ in range(N):
    lst.append(list(map(int,input().split())))
    

print(dfs(0,0))

# print(DP)



