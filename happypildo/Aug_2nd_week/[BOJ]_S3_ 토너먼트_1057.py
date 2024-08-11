"""
# 문제 설명
- 토너먼트 경기를 진행 중에 있다. 지민이와 한수가 A와 B 번호로 출전을 하게 되었다.
- 토너먼트 라운드 대진은 N개의 팀들이 순서대로 묶이게 되고, 지민이와 한수는 둘이 붙지 않는 이상 항상 이긴다.
- 이 때, 지민이와 한수는 몇 번째 라운드에서 만날 것인가>

# 접근 방식
- `N=100,000`이라고 나와 있는데, 그래도 최대 17라운드이기 때문에 brute-force 방식으로 문제를 풀었다.
- 기본 접근 방식은 아래와 같다.
1. 1라운드에서는 2팀끼리 묶이게 된다.
2. 2라운드에서는 1라운드 승자 중 똑같이 2팀끼리 묶이게 된다.
    - 여기서 2라운드에 올라갈 경우의 수가 되는 팀은 4팀이다.
    - 대진은 순서대로 묶이기 때문에 각 라운드 i에서 맨 처음 대진의 경우의 수는 [1, 2, 3, ..., 2 ** i]가 된다.
    - `in` 방식은 복잡도가 `O(N)`이므로, 맨 처음 값(start_idx, 1)와 마지막 값(end_idx, 2**i) 사이에 A와 B가 동시에 존재하는지 확인하여 출력한다.
"""
N, A, B = list(map(int, input().split()))

rounds = 1
teams = [x+1 for x in range(N)]
is_done = True

while is_done:
    num_of_teams = 2 ** rounds
    for offset in range(1, N+1, num_of_teams):
        start_idx = offset
        end_idx = offset + num_of_teams - 1

        if start_idx <= A <= end_idx and start_idx <= B <= end_idx:
            print(rounds)
            is_done = False
            break

    rounds = rounds + 1
