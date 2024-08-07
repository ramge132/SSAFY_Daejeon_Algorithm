'''
# 문제 요약

1. 오름차순으로 현재보다 높은 좌표로 이동하며 방문해야함. 
2. 산을 깍을 쿠폰 한개 있음. 최대 K만큼
>> 최장길이는?



# 문제 생각

1. 어디가 시작좌표?
- 모든 좌표가 최장코스의 시작점 좌표가 될 수는 가능성 있음. 자신으로 부터 오름 차순으로 길이 잘 닦여져 있다면, 답이 될수 있음. Ex) 1-5-9 < 6-7-8-9
- 하지만, 문제에 가장 높은 지점부터 시작한다고 명시. 

2. K만큼 깍을 수 있다면 얼만큼 깍는게 이득일까?
- 등산 기준, 현재 위치 +1 이 되도록 깍으면 최고. 단, K조건을 따져봐야함 



# How to solve?

1. 등산이 아니라 하산을 중심으로 생각
- 등산이라면, 자신보다 크지만 깍아서 이득이 될 수 있는 경우를 찾을 수 없음
Ex) 1 7 
    6 5   -> 등산으로 이동하면 2번이 최대 But, 하산으로 6이나 7을 5보다 많이 깍는다면(K조건이 만족한다면) 4칸 방문 가능!   

- 하산으로 생각한다면, 현재보다 큰 높이가 있을 때 바로 쿠폰을 사용하면 되므로 문제 발생 X, 현재 높이보다 1작은 높이로 깍으면 Best 


2. DFS로 접근
- 최단거리를 찾는 문제가 아님 -> 반드시 BFS 안써도 안된다고 생각
- 쿠폰 조건을 파라미터로 넣어 재귀적으로 호출하는게 더 낫다 생각
>> 모든 경우를 다 따지기 때문에, 최적의 해를 반드시 찾을 수 밖에 없음

2-1. 자신보다 낮은 높이라면?
- 이동

2-2. 자신보다 높은 높이라면? 
- 쿠폰 사용. 단, 쿠폰이 없거나, K값이 부족하다면 이동 못함
- 쿠폰을 사용했다면, 쿠폰을 사용했다는 정보, 깍인 산의 정보를 DFS에 넣어서 재귀 호출

'''


# 1949. [모의 SW 역량테스트] 등산로 조성

# DFS
# i,j: 좌표, depth: 이동거리, ch: 쿠폰
def dfs(i, j, depth,ch): 
    global ans

    # 최장 길이 만족 시, 갱신
    if depth > ans:
        ans = depth

    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni,nj = i + di, j + dj

        # 범위 조건 만족
        if 0 <= ni < N and 0 <= nj < N:

            # 방문하지 않았고, 현재 높이보다 낮은 경우 -> 방문처리, DFS
            if arr[ni][nj] < arr[i][j] and v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(ni, nj, depth + 1,ch)
                v[ni][nj] = 0
            
            # 방문하지 않았고, 현재 높이보다 크거나 같은 경우 -> 쿠폰 조건 만족 시 산깍고, 방문처리, DFS
            elif arr[ni][nj] >= arr[i][j] and v[ni][nj]==0: 
                # 쿠폰이 있고,
                if ch:
                    # 현재보다 낮게 높이를 깍을 수 있다면
                    if arr[ni][nj]-K<arr[i][j]: 
                        ch=False # 쿠폰 사용
                        tmp = arr[ni][nj] # 깍인 산의 정보를 DFS로 호출하기 위해, tmp 받아둠
                        arr[ni][nj]=arr[i][j]-1 # 깍인 산 = 현재 높이-1 
                        v[ni][nj]=1 # 방문 처리
                        dfs(ni,nj,depth+1,ch) # DFS 호출
                        ch=True 
                        v[ni][nj] = 0 
                        arr[ni][nj]=tmp # 높이 복귀


# Main
T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    arr=[]
    ans=0 #  최장경로 길이
    max_H=0 # 최고높이

    # 리스트 생성, 최고 높이 갱신
    for i in range(N):
        arr.append(list(map(int,input().split())))
        max_H=max(max_H,max(arr[i]))

    # 시작점 좌표 저장
    st_point=[]   
    for i in range(N):
        for j in range(N):
            if arr[i][j]==max_H:
                st_point.append((i,j))

    # 방문 체크 리스트
    v = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j]==max_H: # 꼭대기 지점에서 DFS 수행
                v[i][j]=1
                dfs(i,j,1,True)
                v[i][j]=0

    print(f'#{tc}',ans)