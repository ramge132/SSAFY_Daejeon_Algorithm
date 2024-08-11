"""
# 문제 설명
- 랭킹 리스트를 만들 때, 같은 점수가 있다면 그러한 점수의 등수 중 가장 작은 등수를 쓴다.
    - 100, 90, 90, 80일 떄, 각각의 등수는 1, 2, 2, 4등이다.
- 또한, 랭킹 리스트는 P개의 점수만 있을 수 있는데, 이 때 새로운 점수가 들어갈 때 몇등인지 출력하시오.
    - 랭킹 리스트에 오를 수 없다면, -1을 출력한다.

# 접근 방법
- 오름차순으로 정렬하여 새로 들어온 점수의 실제 랭킹(중복 없이 다룬)을 구한다.
- 만약 이 값이 P보다 크다면, 랭킹에 등록될 수 없기에 -1을 출력
- 그렇지 않다면, "그러한 점수의 등수 중 가장 작은 등수"를 찾기 위해 내림차순으로 정렬하여 순위를 찾는다.
"""
N, score, P = list(map(int, input().split()))

if N == 0:
    print("1")
else:
    scores = sorted(list(map(int, input().split())) + [score])
    rank = len(scores) - scores.index(score)
    
    if rank > P:
        print(-1)
    else:
        pass
        scores = sorted(scores, reverse=True)
        print(scores.index(score) + 1)
