
# 1244 최대 상금

'''
접근법

- 그리디하게 접근하기에는 교체횟수 소진 조건이 있으므로 모든 경우의 수를 따져야함

1. 가능한 모든 경우를 처리하되, 교환횟수(cnt)를 종료조건으로 사용하자 

2. 시간 복잡도: 6C2^10 = 15^10 >> 가지치기 필요


- 가지치기 point

1. 중복방지: 같은 숫자에 같은 횟수까지 진행해본 연산에 대해서는 dfs 수행할 필요 x 

2. (교환 횟수, lst 값) -> 중복체크 

3. dfs 수행하고 나서 check 추가 해주기, 재귀 호출한 모든 연산 처리하고 올라온 상태이므로 

'''

# dfs 함수
def dfs(cnt):
    global ans

    if cnt==N:
        # ans 값 비교 후 갱신
        ans=max(ans,int(''.join(map(str,lst))))
        return

    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):

            # swap: 바꾼 경우
            lst[i],lst[j]=lst[j],lst[i]

            # 가지치기
            # cnt: 교체횟수, chk_num: 현재 값
            chk_num=int(''.join(map(str,lst)))
            if (cnt,chk_num) not in check:
                # dfs 호출
                dfs(cnt+1)
                check.append((cnt,chk_num))

            # 원상복구: 안바꾼 경우
            lst[i], lst[j] = lst[j], lst[i]


# main
T=int(input())
for tc in range(1,T+1):

    # num: 숫자카드, cnt: 교체횟수
    num,N=map(int,input().split())

    # 숫자 카드 리스트 변환
    lst=list(map(int,str(num)))

    # 정답
    ans=0

    # 중복 체크
    check=[]

    dfs(0)
    print(f'#{tc}',ans)