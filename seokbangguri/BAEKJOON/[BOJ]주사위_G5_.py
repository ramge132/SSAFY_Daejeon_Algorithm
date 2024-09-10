n = int(input())
dice = list(map(int, input().split()))

five = {
    1: [0,1,2,3,4],
    2: [0,1,2,3,5],
    3: [0,1,2,4,5],
    4: [0,1,3,4,5],
    5: [0,2,3,4,5],
    6: [1,2,3,4,5],
}

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
    12: [3,1]
}

if n == 1:
    min_five = float('inf')
    for a,b,c,d,e in five.values():
        if dice[a] + dice[b] + dice[c] + dice[d] + dice[e] < min_five:
            min_five = dice[a] + dice[b] + dice[c] + dice[d] + dice[e]
    print(min_five)

else:
    min_three = float('inf')
    min_two = float('inf')

    for a, b in two.values():
        if dice[a] + dice[b] < min_two:
            min_two = dice[a] + dice[b]

    for a, b, c in three.values():
        if dice[a] + dice[b] + dice[c] < min_three:
            min_three = dice[a] + dice[b] + dice[c]
    
    if n == 2:
        print(min_three*4 + min_two*4)
    else:
        # 옆면 + 윗면 + 모서리 세로 + 모서리 가로 + 꼭지점 4개
        result = (min(dice) * (n-2)**2 * 5) + (min_two * (n-1) * 4) + (min_two * (n-2) * 4) + (min_three * 4) + (min(dice) * (n-2) * 4)
        print(result)