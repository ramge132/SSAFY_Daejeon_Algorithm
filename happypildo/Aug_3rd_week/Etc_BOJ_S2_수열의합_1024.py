"""
# 문제 설명
- N과 L이 주어진다. 이를 기반으로 우리는 배열을 만들어야 하는데 
    - 1) 배열의 합은 N 이여야 하고, 
    - 2) 배열의 길이는 최소 L이여야 한다.
    - 3) 배열의 값은 순차적이여야 한다. (e.g., [3, 4, 5, 6])
- 이 때, 배열을 출력하시오.
    - 만들 수 없거나, 100개 초과의 배열 요소를 가질 경우 -1을 출력한다.

# 접근 방법
- N의 범위가 1,000,000,000이기 때문에 완탐으로 풀 수 없다고 생각을 먼저 했습니다.
- 따라서, 조건을 찾고자 하였고
    - L이 짝수일 경우 N / L = *.5 형태로 값이 나와야 함 (숫자가 연속해야 되기 때문)
        - 가운데 값을 `int(N/L)`과 `int(N/L) + 1` 을 기준으로 int((L - 2) / 2) 개씩 붙임
    - L이 홀수일 경우 N / L = 정수 값으로 나와야 함 (숫자가 연속해야 되기 때문)
        - 가운데 값을 `int(N / L)`을 기준으로 해서 int(remain_nums / 2) 개씩 붙임
"""
N, L = list(map(int, input().split()))

answer_list = []
while L < 101:
    if L % 2 == 0:
        if (N / L - 0.5) == int(N/L):
            # 남은 붙여야 할 수 : L - 2
            if int(N / L) - int((L - 2) / 2) >= 0:
                # 만들 수 있음
                answer_list = [int(N/L), int(N/L) + 1]

                left_temp = []
                for left in range(int(N / L) - int((L - 2) / 2), int(N/L)):
                    left_temp.append(left)
                answer_list = left_temp + answer_list
                for right in range(int(N / L) + 2, int(N / L) + 1 + int((L - 2) / 2) + 1):
                    answer_list.append(right)
                break
            else:
                pass
        else:
            pass
    else:
        if (N / L) == int(N / L):
            remain_nums = L - 1
            if 0 <= int(N / L) - int(remain_nums / 2):
                # 만들 수 있음
                answer_list = [int(N / L)]
                left_temp = []
                for left in range(int(N / L) - int(remain_nums / 2), int(N/L)):
                    left_temp.append(left)
                answer_list = left_temp + answer_list
                for right in range(int(N/L)+1, int(N / L) + int(remain_nums / 2) + 1):
                    answer_list.append(right)
                break
            else:
                # 못만듦
                pass
        else:
            pass
    L += 1

if answer_list:
    for val in answer_list:
        print(f"{val} ", end="")
    print()
else:
    print(-1)