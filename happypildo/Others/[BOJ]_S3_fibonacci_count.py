"""
문제 설명:
피보나치 재귀 함수에서는, 0과 1에서 return이 호출된다.
n이 주어졌을 때, 피보나치 재귀 함수에서 0과 1이 각각 몇 번 호출되는지 출력하라.

해피필도 팁:
운 좋게 입출력 케이스에서 통찰을 얻어서 따로 없읍니다...
혹시나 해서 재귀함수를 직접 만들고 카운트를 해 보았는데, n=40일 때 복잡도가 2^40승이라 답 안나옵니다.
-> memoization을 사용하면 효과적이겠지만, 0과 1을 카운트해야해서 사용하지 않았습니다.
"""
DP_table = [[1, 0], [0, 1]]

for n in range(2, 41):
    new_value = [DP_table[n-2][0] + DP_table[n-1][0], DP_table[n-2][1] + DP_table[n-1][1]]
    DP_table.append(new_value)

T = int(input())
for _ in range(T):
    n = int(input())
    answer = DP_table[n]

    print(answer[0], answer[1])