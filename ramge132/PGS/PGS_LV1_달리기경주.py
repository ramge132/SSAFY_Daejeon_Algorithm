# https://school.programmers.co.kr/learn/courses/30/lessons/178871

# 선수들이 경주 중 추월하는 상황을 추적하여 최종 순위를 구하는 문제.
# 분류: 구현
# 시간복잡도: O(n + m) / n은 players의 길이, m은 callings의 길이.

def solution(players, callings):
    # 선수 이름을 키, 현재 순위를 값으로 하는 딕셔너리 생성
    player_dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_dict[call]
        # 추월한 선수의 현재 순위가 0보다 큰 경우 (1등이 아닌 경우에만)
        if idx > 0:
            # 현재 선수의 앞에 있는 선수 이름
            previous_player = players[idx - 1]
            # 현재 선수와 앞의 선수의 순위 교환
            player_dict[previous_player], player_dict[call] = player_dict[call], player_dict[previous_player]
            # 선수 배열에서도 순위 교환
            players[idx - 1], players[idx] = players[idx], players[idx - 1]
    
    return players