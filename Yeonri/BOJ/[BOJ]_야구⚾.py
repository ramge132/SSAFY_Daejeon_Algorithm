from itertools import permutations
N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
max_total = 0

def chk(inning, current_player):
    global d1, d2, d3, last_player, out
    if lst[inning][players[current_player]] == 0:
        out += 1
        last_player = (last_player + 1) % 9 # 나머지를 이용해서 순환
        return 0
    
    if lst[inning][players[current_player]] == 1:
        score = d3
        d1, d2, d3 = 1, d1, d2
        last_player = (last_player + 1) % 9
        return score
    
    if lst[inning][players[current_player]] == 2:
        score = d2 + d3
        d1, d2, d3 = 0, 1, d1
        last_player = (last_player + 1) % 9
        return score
    
    if lst[inning][players[current_player]] == 3:
        score = d1 + d2 + d3
        d1, d2, d3 = 0, 0, 1
        last_player = (last_player + 1) % 9
        return score
    
    if lst[inning][players[current_player]] == 4:
        score = 1 + d1 + d2 + d3
        d1, d2, d3 = 0, 0, 0
        last_player = (last_player + 1) % 9
        return score


for perm in permutations(range(1,9)):
    players = list(perm[:3]) + [0] + list(perm[3:]) # 4번을 첫번 째 선수로 고정
    total = 0 # 각 순열마다 점수 초기화
    last_player = 0 # 새로운 타순 초기화 및 최근 플레이어 idx 저장

    for inning in range(N): # 각 이닝 반복
        d1, d2, d3 = 0, 0, 0 # 진루 주자 초기화
        out = 0 # 아웃 초기화
        
        while out < 3: 
            total += chk(inning, last_player)

    if max_total < total:
        max_total = total

print(max_total)


# from itertools import permutations

# def chk(player_num):
#     global score, runners

#     if player_num == 0:
#         return False
    
#     temp_runners = runners
#     runners = 0
    
#     for i in range(3, -1, -1): # 3 ~ 0 까지의 위치를 확인한다.
#         if i == 0 or (temp_runners & (1 << i)): # & 연산자를 이용해 해당 위치에 주자 존재 확인
#             new_pos = i + player_num # 타자의 위치 이동
#             if new_pos >= 4: # 홈으로 들어왔을 때 점수 증가
#                 score += 1
#             else:
#                 runners |= (1 << new_pos) # or를 사용해서  비트를 합쳐준다. 

#     return True

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]

# max_score = 0
# players = []

# for numbers in permutations(range(1,9)):
#     player = list(numbers[:3]) + [0] + list(numbers[3:])
#     score = 0
#     ground = 0
#     cnt = 1
#     idx = 0
#     for i in range(N):
#         out = 0
#         ground = 0
#         runners = 0b0000
#         while out < 3:
#             if chk(lst[i][player[idx]]):
#                 pass
#             else:
#                 out += 1
#             idx = (idx + 1) % 9

#     # print(player, score)
#     max_score=max(max_score, score)

# print(max_score)



# def dfs(player):
#     global players

#     if len(player) == 9:
#         players.append(player)
#         return


#     if len(player) == 3: # 첫번째 플레이어는 4번으로 정해져 있으므로 넘김
#             dfs(player + [0])
#             return

#     for i in range(1, 9):   
#         if i not in player:    
#             # 플레이어 선택
#             dfs(player + [i])


# def chk(player_num):
#     global score, runners

#     if player_num == 0:
#         return False
    
#     temp_runners = runners
#     runners = 0
    
#     # 기존 주자 + 타자 진루
#     for i in range(3, -1, -1):
#         if i == 0 or (temp_runners & (1 << i)):
#             new_pos = i + player_num
#             if new_pos >= 4:
#                 score += 1
#             else:
#                 runners |= (1 << new_pos)

#     return True

# N = int(input())
# lst = [list(map(int, input().split())) for _ in range(N)]

# max_score = 0
# players = []
# dfs([])

# for player in players:
#     score = 0
#     ground = 0
#     cnt = 1
#     idx = 0
#     for i in range(N):
#         out = 0
#         ground = 0
#         runners = 0b0000
#         while out < 3:
#             if chk(lst[i][player[idx]]):
#                 pass
#             else:
#                 out += 1
#             idx = (idx + 1) % 9

#     # print(player, score)
#     max_score=max(max_score, score)

# print(max_score)