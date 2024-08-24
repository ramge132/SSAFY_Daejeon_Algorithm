figures = [1,2,3]

def dfs(a):
    global result
    if a == 0:
        result += 1
        return
    
    for f in figures:
        if f <= a:
            a -= f
            dfs(a)
            a += f


N = int(input())
for _ in range(N):
    a = int(input())
    result = 0
    dfs(a)
    print(result)