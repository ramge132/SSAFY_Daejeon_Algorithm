# https://www.acmicpc.net/problem/17136

def can_place(x, y, size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(size):
        for j in range(size):
            if grid[x + i][y + j] != 1:
                return False
    return True

def place_paper(x, y, size, value):
    for i in range(size):
        for j in range(size):
            grid[x + i][y + j] = value

def backtrack(idx, count):
    global min_papers

    if idx == 100:
        min_papers = min(min_papers, count)
        return

    x = idx // 10
    y = idx % 10

    if grid[x][y] == 1:
        for size in range(5, 0, -1):
            if papers[size] > 0 and can_place(x, y, size):
                place_paper(x, y, size, 0)
                papers[size] -= 1
                backtrack(idx + 1, count + 1)
                place_paper(x, y, size, 1)
                papers[size] += 1
    else:
        backtrack(idx + 1, count)

grid = [list(map(int, input().split())) for _ in range(10)]
papers = [0, 5, 5, 5, 5, 5]
min_papers = float('inf')

backtrack(0, 0)

if min_papers == float('inf'):
    print(-1)
else:
    print(min_papers)