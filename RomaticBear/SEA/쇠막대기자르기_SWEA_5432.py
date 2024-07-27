# 5432 쇠막대기 자르기

t=int(input())
for tc in range(1,t+1):
    lst=input()
    lst=lst.replace('()','*')

    ans=0 # 잘린 총 막대
    cnt=0 # 막대 개수

    for i in range(len(lst)):
        if lst[i]=='*':
            ans+=cnt

        elif lst[i]=='(':
            cnt+=1

        else:
            cnt-=1
            ans+=1

    print(f'#{tc}',ans)