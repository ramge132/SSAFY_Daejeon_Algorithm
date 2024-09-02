import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T + 1):
    string = sorted(list(input()))
    string_set = set(string)
    for s in list(string_set):
        # 짝수
        if not string.count(s)%2:
            # remove()는 해당 요소가 없으면 KeyError
            # string_set.remove(s)
            # discard()는 해당 요소가 없어도 정상 종료
            string_set.discard(s)
    if len(string_set):
        print(f'#{test_case} {"".join(sorted(list(string_set)))}')
        continue

    print(f'#{test_case} Good')
