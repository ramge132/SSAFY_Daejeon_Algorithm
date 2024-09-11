# input
"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""

T = int(input())
for test_case in range(T):
    N = int(input())
    wears = {}
    for _ in range(N):
        wear, type = input().split()
        if wears.get(type):
            wears[type].append(wear)
        else:
            wears[type] = [wear]

    settings = 1
    for t in wears:
        settings *= len(wears[t]) + 1
    
    print(settings - 1)
            