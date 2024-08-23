# 경로가 유일하지 않은 경우가 있을까?
"""
# 문제 설명:
- 여러 여행 티켓이 주어지고, 하나의 여행 티켓은 출발지와 목적지로 구성되어 있다. 여기서, 출발지와 목적지는 세 글자이다.
- "ICN"이라는 공항에서 출발하여 모든 여행 티켓을 사용하고자 하는데, 동선이 여러개 생길 경우 알파벳 순서로 진행한다.
- 예를 들어,
    - [ICN, ABC]와 [ICN, BAC]가 있다면 알파벳 순으로 진행하여 ABC 공항을 먼저 간다.
- 이 때, 순회되는 여행지를 순서대로 출력하시오.

# 접근 방법:
- 처음에 문제 조건이 자세하지 않아서 별 생각이 없었지만 "동일한 티켓이 여러 개 있을 수 있다"를 생각해 내어 풀 수 있었다.
- DFS로 풀었으며, 중첩된 티켓을 반영하기 위해 방문 set을 사용하지 않고 dictionary를 사용했다.
    - 예) [ICN, ABC]: 2 -> 2번 방문되어야 함을 의미
"""
import copy 
fastest_path = ""
def DFS(source, path_dict, ticket_arr, ticket_dict, travel):
    global fastest_path
    if path_dict.get(source, None) is None:
        # if len(travel) == len(ticket_arr) * 3 * 2:
        if ticket_dict['visited_tickets'] == 0:
            if fastest_path > travel:
                fastest_path = travel
        return
    # if len(travel) == len(ticket_arr) * 3 * 2:
    if ticket_dict['visited_tickets'] == 0:
        if fastest_path > travel:
            fastest_path = travel
        return
    
    if travel > fastest_path:
        return
    
    for destination in path_dict[source]:
        if ticket_dict[(source, destination)] != 0:
            temp_ticket_dict = copy.deepcopy(ticket_dict)
            temp_ticket_dict[(source, destination)] -= 1 
            temp_ticket_dict['visited_tickets'] -= 1

            DFS(destination, path_dict, ticket_arr, temp_ticket_dict, travel + f"{source}{destination}")


def solution(tickets):
    global fastest_path

    path_dict = {}
    ticket_arr = []
    ticket_dict = {}
    for source, destination in tickets:
        ticket_arr.append((source, destination))

        if ticket_dict.get((source, destination), None) is None:
            ticket_dict[(source, destination)] = 1
        else:
            ticket_dict[(source, destination)] += 1
        if path_dict.get(source, None) is None:
            path_dict[source] = [destination]
        else:
            path_dict[source].append(destination)
    ticket_dict["num_of_tickets"] = len(tickets)
    ticket_dict["visited_tickets"] = len(tickets)

    fastest_path = "a" * ticket_dict["num_of_tickets"] * 3 * 2
    DFS(source="ICN", path_dict=path_dict, ticket_arr=ticket_arr, ticket_dict=ticket_dict, travel="")
    
    # PROCESSING
    answer = []
    for offset in range(0, len(fastest_path), 6):
        answer.append(fastest_path[offset:offset+3])
    answer.append(fastest_path[-3:])

    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"], ["SFO", "ICN"]]))
print(solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "ICN"]]))
# print(
#     solution(
#         [["ICN", "A"], ["ICN", "B"], ["ICN", "C"], ["A", "AA"], ["A", "BB"]]
#     )
# )