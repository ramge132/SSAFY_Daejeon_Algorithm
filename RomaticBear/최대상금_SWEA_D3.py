# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
'''
두 자리 수를 바꿔가면 교환 횟수가 N이 될때까지 재귀 호출
백트랙킹 원리: 교체 -> 재귀호출 -> 원위치 

'''

def dfs(n,lst):
    global ans

    if n==K:
        num=int(''.join(map(str,lst)))
        ans=max(ans,num)
        return

    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst[i],lst[j]=lst[j],lst[i]
            check = int(''.join(map(str, lst)))
            if (n,check) not in v:
                v.append((n,check))
                dfs(n+1,lst)
            lst[i],lst[j]=lst[j],lst[i]

T=int(input())
for tc in range(1,T+1):
    N,K=map(int,input().split())
    lst=list(map(int,str(N)))
    ans=0
    v=[]
    dfs(0,lst)
    print(f'#{tc}',ans)
    