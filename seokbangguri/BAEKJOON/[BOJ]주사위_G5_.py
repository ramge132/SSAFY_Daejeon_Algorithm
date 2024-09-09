n = int(input())
dice = list(map(int, input().split()))

three = {
    1: [0,1,3],
    2: [0,1,2],
    3: [0,2,4],
    4: [0,3,4],
    5: [5,1,2],
    6: [5,1,3],
    7: [5,3,4],
    8: [5,2,4]
}

two = {
    1: [0,1],
    2: [0,2],
    3: [0,3],
    4: [0,4],
    5: [5,1],
    6: [5,2],
    7: [5,3],
    8: [5,4],
    9: [1,2],
    10: [2,4],
    11: [4,3],
    12: [3,2]
}

min_three = float('inf')
min_two = float('inf')

for a, b in two.values():
    if dice[a] + dice[b] < min_two:
        min_two = dice[a] + dice[b]


for a, b, c in three.values():
    if dice[a] + dice[b] + dice[c] < min_three:
        min_three = dice[a] + dice[b] + dice[c]

result = ((n-2)**2 * 5) + (min_two**2 * (n-1)*(n-2) * 16) + (min_three * 4) + ((n-2)*4)
print(result)