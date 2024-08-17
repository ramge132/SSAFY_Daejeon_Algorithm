"""
# 문제 설명
- N 명의 사람이 있고 이들은 서로 친구일 수도, 또는 서로 2-친구일 수도 있다.
- A가 B의 2-친구라 함은 아래와 같다.
    - A와 B가 친구이다.
    - A와 B 둘과 친구인 C가 존재한다.
- 위와 같을 때, 가장 인기 있는 (친구가 많은) 사람의 친구 수를 구하시오.

# 접근법
- 먼저 1:1로 친구인 사람을 friend dict에 넣어주었습니다. 
    - dict 구조) 사람 인덱스: 친구들 인덱스 (set)
- 이후, 한 단계 더 나아가 second-friend를 찾아 주었습니다.
"""
N = int(input())

friend_dict = {x: set() for x in range(N)}

for n_iter in range(N):
    line = input()

    for friend_idx, is_friend in enumerate(line):
        if is_friend == 'Y':
            friend_dict[n_iter].add(friend_idx)

answer = -1
for n_iter in range(N):
    friend_set = friend_dict[n_iter]

    second_friends = set()
    for friend_idx in friend_set:
        # find second-friend
        for second_friend_idx in friend_dict[friend_idx]:
            if n_iter != second_friend_idx:
                second_friends.add(second_friend_idx)
    
    total_friends = len(friend_dict[n_iter] | second_friends)
    if answer < total_friends:
        answer = total_friends

print(answer)
