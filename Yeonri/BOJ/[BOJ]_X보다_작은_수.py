N, X = map(int,input().split())
A = list(map(int,input().split()))

# A에서 X보다 작은 수를 출력한다.
for i in A: # O(N)
    if i < X: # O(1) 탐색이기 때문
        print(i,end = ' ')