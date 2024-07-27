# [모의 SW 역량테스트] 활주로 건설
# 알고리즘 분류: 그리디
# 시간 복잡도: O(T * N^2)
# 각 행과 열을 한 번씩 탐색하며 경사로 설치 가능 여부를 확인하기 때문

def can_build_runway(line, X):
    N = len(line)
    used = [False] * N  # 각 셀에 경사로가 이미 사용되었는지 여부를 추적하기 위한 배열

    for i in range(1, N):
        if line[i] == line[i - 1]:
            continue  # 현재 셀과 이전 셀이 높이가 같은 경우, 다음 셀로 이동
        elif line[i] - line[i - 1] == 1:
            # 현재 셀이 이전 셀보다 높이가 1 높은 경우
            for j in range(1, X + 1):
                # 경사로 길이만큼 이전 셀을 확인
                if i - j < 0 or line[i - j] != line[i - 1] or used[i - j]:
                    return False  # 경사로를 설치할 수 없는 경우
            for j in range(1, X + 1):
                used[i - j] = True  # 경사로 설치를 표시
        elif line[i - 1] - line[i] == 1:
            # 현재 셀이 이전 셀보다 높이가 1 낮은 경우
            for j in range(X):
                # 경사로 길이만큼 다음 셀을 확인
                if i + j >= N or line[i + j] != line[i] or used[i + j]:
                    return False  # 경사로를 설치할 수 없는 경우
            for j in range(X):
                used[i + j] = True  # 경사로 설치를 표시
        else:
            return False  # 높이 차이가 1 이상인 경우, 경사로를 설치할 수 없음

    return True  # 모든 조건을 만족하면 경사로 설치 가능

T = int(input().strip())

for t in range(1, T + 1):
    # 지형의 크기 N과 경사로의 길이 X 입력
    N, X = map(int, input().strip().split())
    
    # 지형 정보를 2차원 리스트로 입력
    grid = [list(map(int, input().strip().split())) for _ in range(N)]
    
    total_runways = 0  # 활주로를 건설할 수 있는 경우의 수를 저장할 변수
    
    # 가로 방향 활주로 검사
    for row in grid:
        if can_build_runway(row, X):
            total_runways += 1  # 활주로를 건설할 수 있는 경우 추가
    
    # 세로 방향 활주로 검사
    for col in range(N):
        column = [grid[row][col] for row in range(N)]
        if can_build_runway(column, X):
            total_runways += 1  # 활주로를 건설할 수 있는 경우 추가
    
    print(f"#{t} {total_runways}")
