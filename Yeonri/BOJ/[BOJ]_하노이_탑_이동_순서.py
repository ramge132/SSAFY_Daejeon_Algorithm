# 원판 n개를 a번 기둥에서 b번 기둥으로 옮기는 방법
# n = 1 일때 base condition
# n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다.
# n번 원판을 기둥 a에서 기둥 b로 옮긴다.
# n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다.

K = int(input())

# 원판 n개를 a기둥에서 b기둥이로 이동
# base condition n = 1일때, 마지막으로 옮긴다.
# 기둥 숫자의 총 합 = 6, 6-a-b = 2 >> 2번 기둥으로 옮긴다.
# n-1개는 3번기둥에서 3기둥으로 이동 >> 6-a-b

def hanoi(a,b,n):
    # base condition
    if n == 1:
        print(f'{a} {b}')
        return

    hanoi(a,6-a-b,n-1)
    print(f'{a} {b}')
    hanoi(6-a-b,b,n-1)

print(f'{2**K-1}')
hanoi(1,3,K)


