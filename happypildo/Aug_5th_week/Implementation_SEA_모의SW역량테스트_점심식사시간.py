"""
사용해본 조기 종료 조건
- 예상되는 종료 시간을 하한으로서 정의
```python
expected_end_time_as_lower_bound = sum([len(time_to_stairs[s]) // 3 * self.stairs[s].len for s in range(2)])
if simulation_tik + expected_end_time_as_lower_bound > prev_answer: return float('inf')
```
    - 647ms로, 이를 계산하는데 시간이 더 걸리는 것 같음
"""

from itertools import combinations 
import heapq


class Stair:
    def __init__(self, stair_length, stair_location):
        self.len = stair_length
        self.loc = stair_location
        self.waiting_queue = []


class Person:
    def __init__(self, location, stairs):
        self.loc = location
        self.time_to_stairs = [
            abs(self.loc[0] - stair.loc[0]) + abs(self.loc[1] - stair.loc[1]) for stair in stairs
        ]


class Hall:
    def __init__(self, N, stair_info, person_info):
        self.N = N
        self.stairs = [Stair(*stair) for stair in stair_info]
        self.num_of_stairs = len(self.stairs)
        self.people = [Person(*person, self.stairs) for person in person_info]
        self.num_of_people = len(self.people)

    def search_all(self):
        total_person_idx = set(x for x in range(self.num_of_people))

        answer = float('inf')
        for i in range(self.num_of_people + 1):
            for subset in combinations(total_person_idx, i):
                people_for_stair1 = set(subset)
                people_for_stair2 = total_person_idx - people_for_stair1

                ret = self.make_solution([people_for_stair1, people_for_stair2], answer)
                answer = ret if ret < answer else answer
        
        return answer

    def make_solution(self, people_for_stairs, prev_answer):
        time_to_stairs = [[], []]
        for s_idx, people_for_stair in enumerate(people_for_stairs):
            for p_idx in people_for_stair:
                heapq.heappush(time_to_stairs[s_idx], [self.people[p_idx].time_to_stairs[s_idx], p_idx])

        simulation_tik = 0
        while True:
            # 조기 종료 조건을 넣어보자
            if simulation_tik > prev_answer: return float('inf')

            for s_idx, time_to_stair in enumerate(time_to_stairs):
                # 먼저 뺄 수 있는 사람이 있으면 뺴주자
                temp_waiting_queue = []
                for remain_time, person_idx in self.stairs[s_idx].waiting_queue:
                    if remain_time != 0:
                        # 아직 남았어요, 시간 하나 빼자
                        # temp_waiting_queue.append([remain_time - 1, person_idx])
                        if remain_time - 1 == 0:
                            continue
                        else:
                            temp_waiting_queue.append([remain_time - 1, person_idx])
                self.stairs[s_idx].waiting_queue = temp_waiting_queue[:]

                # 지금 사람을 넣을 수 있다면 넣자
                # 고려해야할 점:
                    # 지금 계단이 비어 있는지
                    # 사람이 계단에 도착했는지
                if time_to_stair:
                    while True:
                        if not time_to_stair:
                            break
                        if len(self.stairs[s_idx].waiting_queue) == 3:
                            break
                        else:
                            eta, p_idx = time_to_stair[0]
                            if eta < simulation_tik:        # 도착 후 1초 기다려야 한다.
                                _, p_idx = heapq.heappop(time_to_stairs[s_idx])
                                self.stairs[s_idx].waiting_queue.append([self.stairs[s_idx].len, p_idx])
                            else:
                                break

            simulation_tik += 1

            # 두 힙이 모두 비어 있고, 계단에 사람이 없으면 끝이다.
            is_finish = len(time_to_stairs[0]) == 0 and len(time_to_stairs[1]) == 0 and len(self.stairs[0].waiting_queue) == 0 and len(self.stairs[1].waiting_queue) == 0
            if is_finish:
                simulation_tik -= 1
                break
        
        return simulation_tik


T = int(input())
for t_iter in range(1, T+1):
    N = int(input())

    input_map = []
    person_info = []
    stair_info = []
    for i in range(N):
        input_line = list(map(int, input().split()))
        for j, item in enumerate(input_line):
            if input_line[j] == 1:
                # Person
                person_info.append([[i, j]])
            elif input_line[j] > 1:
                # Stair
                stair_info.append([input_line[j], [i, j]])

    h = Hall(N, stair_info, person_info)
    print(f"#{t_iter} {h.search_all()}")