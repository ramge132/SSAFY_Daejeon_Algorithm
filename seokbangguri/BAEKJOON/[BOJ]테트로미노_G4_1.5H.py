tetromino = {
    1: [[True]*4],
    2: [[True]*2]*2,
    3: [[True, False],[True, False],[True, True]],
    4: [[True, False],[True, True],[False, True]],
    5: [[True]*3,[False, True, False]]
}

# 테트로미노 하나 당 최대 8가지 모양 
def changeShape(tetro, change_no):
    '''
    - tetro: 테트로노미노
    - change_no: 변경 할 모양
        1. 그대로
        2. 좌우반전
        3. 상하반전
        4. 좌우반전 and 상하반전
        5. 90도 회전
        6. 90도 회전 후 좌우반전
        7. 90도 회전 후 상하반전
        8. 90도 회전 후 좌우반전 and 상하반전
    '''
    if change_no == 1:
        return tetro

    elif change_no == 2:
        for i in range(len(tetro)):
            tetro[i] = tetro[i][::-1]
        return tetro

    elif change_no == 3:
        return tetro[::-1]

    elif change_no == 4:
        for i in range(len(tetro)):
            tetro[i] = tetro[i][::-1]
        return tetro[::-1]

    # 여기부터 기본 90도 회전
    else:
        tetro = list(zip(*tetro))[::-1]

        if change_no == 5:
            return tetro

        elif change_no == 6:
            for i in range(len(tetro)):
                tetro[i] = tetro[i][::-1]
            return tetro

        elif change_no == 7:
            return tetro[::-1]

        elif change_no == 8:
            for i in range(len(tetro)):
                tetro[i] = tetro[i][::-1]
            return tetro[::-1]


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
result = 0

for t in tetromino:
    for i in range(1, 9):
        test_tetromino = changeShape([a[:] for a in tetromino[t]], i)
        
        # 테트로노미노의 가로, 세로 길이
        x_length = len(test_tetromino[0])
        y_length = len(test_tetromino)

        # 테트로노미노를 놓을 좌측 위 좌표
        for y in range(N - y_length + 1):
            for x in range(M - x_length + 1):
                temp_result = 0
                for ty in range(y_length):
                    for tx in range(x_length):
                        if test_tetromino[ty][tx]:
                            temp_result += matrix[y + ty][x + tx]
                if result < temp_result:
                    result = temp_result

print(result)