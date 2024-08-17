import sys
sys.stdin = open('input.txt')
figures = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for test_case in range(1, T + 1):
    N = int(list(map(str, input().split()))[1])
    strings = list(map(str, input().split()))
    result = f'#{test_case}\n'

    for x in figures:
        times = strings.count(x)
        result += (x + ' ') * times

    print(result)