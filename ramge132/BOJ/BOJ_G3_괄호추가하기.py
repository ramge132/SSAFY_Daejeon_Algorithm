# https://www.acmicpc.net/problem/16637

def calculate(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def dfs(index, current_value):
    global max_value
    if index >= len(numbers) - 1:
        max_value = max(max_value, current_value)
        return
    
    # 괄호 없이 다음 연산 수행
    next_value = calculate(operators[index], current_value, numbers[index + 1])
    dfs(index + 1, next_value)
    
    # 괄호를 사용하여 연산 (다음 연산자와 숫자 먼저 계산)
    if index + 1 < len(operators):
        next_value_with_bracket = calculate(operators[index + 1], numbers[index + 1], numbers[index + 2])
        next_value = calculate(operators[index], current_value, next_value_with_bracket)
        dfs(index + 2, next_value)

# 입력
n = int(input())
expression = input()

numbers = []
operators = []

for i in range(n):
    if i % 2 == 0:
        numbers.append(int(expression[i]))
    else:
        operators.append(expression[i])

max_value = float('-inf')
dfs(0, numbers[0])

print(max_value)
