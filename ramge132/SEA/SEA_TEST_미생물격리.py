# [모의 SW 역량테스트] 미생물 격리
# 알고리즘 분류: 시뮬레이션
# 시간 복잡도: O(M * K)
# M 시간 동안 각 K개의 미생물 군집을 이동시키며 처리

# 미생물 군집 정보를 나타내는 클래스 정의
class MicroGroup:
    def __init__(self, y, x, count, direction):
        self.y = y
        self.x = x
        self.count = count
        self.direction = direction

# 방향에 대한 정의 (상, 하, 좌, 우)
DIRECTION = {
    1: (-1, 0),  # 상
    2: (1, 0),   # 하
    3: (0, -1),  # 좌
    4: (0, 1)    # 우
}

# 반대 방향을 정의
REVERSE_DIRECTION = {
    1: 2,  # 상 -> 하
    2: 1,  # 하 -> 상
    3: 4,  # 좌 -> 우
    4: 3   # 우 -> 좌
}

T = int(input().strip())

for t in range(1, T+1):
    N, M, K = map(int, input().strip().split())
    
    # 군집 정보를 저장할 리스트
    microbes = []
    
    for _ in range(K):
        y, x, count, direction = map(int, input().strip().split())
        microbes.append(MicroGroup(y, x, count, direction))
    
    # M 시간 동안 시뮬레이션 수행
    for _ in range(M):
        # 다음 위치에 대한 정보 저장
        new_positions = {}
        
        for microbe in microbes:
            # 현재 미생물 군집의 이동
            dy, dx = DIRECTION[microbe.direction]
            ny, nx = microbe.y + dy, microbe.x + dx
            
            # 약품이 칠해진 셀로 이동한 경우
            if ny == 0 or ny == N-1 or nx == 0 or nx == N-1:
                microbe.count //= 2
                microbe.direction = REVERSE_DIRECTION[microbe.direction]
            
            if microbe.count > 0:
                if (ny, nx) in new_positions:
                    new_positions[(ny, nx)].append(microbe)
                else:
                    new_positions[(ny, nx)] = [microbe]
            
            microbe.y, microbe.x = ny, nx
        
        # 군집이 합쳐지는 경우 처리
        new_microbes = []
        
        for key in new_positions:
            if len(new_positions[key]) > 1:
                max_count = 0
                max_direction = None
                total_count = 0
                
                for microbe in new_positions[key]:
                    total_count += microbe.count
                    if microbe.count > max_count:
                        max_count = microbe.count
                        max_direction = microbe.direction
                
                new_microbes.append(MicroGroup(key[0], key[1], total_count, max_direction))
            else:
                new_microbes.append(new_positions[key][0])
        
        microbes = new_microbes
    
    # 최종 남아 있는 미생물 수의 총합 계산
    total_microbes = sum(microbe.count for microbe in microbes)
    
    print(f"#{t} {total_microbes}")
