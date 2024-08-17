from itertools import permutations

def chk(player_num):
    global score, runners

    if player_num == 0:
        return False
    
    temp_runners = runners
    runners = 0
    
    # 기존 주자 + 타자 진루
    for i in range(3, -1, -1):
        if i == 0 or (temp_runners & (1 << i)):
            new_pos = i + player_num
            if new_pos >= 4:
                score += 1
            else:
                runners |= (1 << new_pos)

    return True

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

max_score = 0
players = []

for numbers in permutations(range(1,9)):
    player = list(numbers[:3]) + [0] + list(numbers[3:])
    score = 0
    ground = 0
    cnt = 1
    idx = 0
    for i in range(N):
        out = 0
        ground = 0
        runners = 0b0000
        while out < 3:
            if chk(lst[i][player[idx]]):
                pass
            else:
                out += 1
            idx = (idx + 1) % 9

    # print(player, score)
    max_score=max(max_score, score)

print(max_score)



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