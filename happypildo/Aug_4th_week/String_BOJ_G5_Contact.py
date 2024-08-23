"""
# 문제 링크: https://www.acmicpc.net/problem/1013
# 문제 설명:
- 문제 참고 하십쇼
# 접근 방법:
"""
N = 200

patterns = {x: set() for x in range(N+10)}
def generate_pattern(repeat_str, concat_str, N):
    global patterns

    temp_str = concat_str[0] + concat_str[1]
    if temp_str in patterns[len(temp_str)]: return
    else: patterns[len(temp_str)].add(temp_str)
    if len(temp_str) > N: return

    generate_pattern(repeat_str, [concat_str[0] + repeat_str[0], concat_str[1] + repeat_str[1]], N)
    generate_pattern(repeat_str, [concat_str[0], concat_str[1] + repeat_str[1]], N)
    generate_pattern(repeat_str, [concat_str[0] + repeat_str[0], concat_str[1]], N)

generate_pattern(["0", "1"], ["100", "1"], N)
patterns[0].add("")
patterns[2].add("01")

def is_valid(remain):
    if remain in patterns[len(remain)]:
        return True
    
    temp_remain = remain[:]
    if remain[0:2] == "01":
        temp_remain = temp_remain[2:]
        
    ret = False
    for seg_len in range(len(temp_remain), 0, -1):
        if temp_remain[:seg_len] in patterns[seg_len]:
            # print(patterns[seg_len], seg_len, temp_remain[:seg_len], temp_remain[seg_len:])
            ret = ret | is_valid(temp_remain[seg_len:])
    return ret

T = int(input())
for t_iter in range(1, T+1):
    input_line = input().rstrip()

    if is_valid(input_line):
        print("YES")
    else:
        print("NO")