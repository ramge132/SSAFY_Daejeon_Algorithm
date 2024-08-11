max_cores = -1
min_lines = float('inf')


def solution(visited_loc, loc_of_cores, circuit, target_core_idx, num_of_linked_lines, num_of_linked_cores):
    global max_cores
    global min_lines
    
    if loc_of_cores.get(target_core_idx, -1) == -1:
        if max_cores < num_of_linked_cores:
            max_cores, min_lines = num_of_linked_cores, num_of_linked_lines
        elif max_cores == num_of_linked_cores:
            if min_lines > num_of_linked_lines:
                min_lines = num_of_linked_lines
        return
    else:
        if num_of_linked_lines > min_lines and num_of_linked_cores < max_cores:
            # 더 봐야 하는데, 이미 연결한 수가 최소 값보다 작을 경우는 더 볼 필요 없다.
            return

    loc_of_core = loc_of_cores[target_core_idx]

    start_end_for = {
        0: [0, loc_of_core[0]],
        1: [loc_of_core[0]+1, len(circuit)],
        2: [0, loc_of_core[1]],
        3: [loc_of_core[1]+1, len(circuit)],
        4: [-1, -1]
    }
    for dir in start_end_for.keys():
        if dir == 4:
            solution(visited_loc, loc_of_cores, circuit, target_core_idx+1, num_of_linked_lines, num_of_linked_cores)
        else:
            s, e = start_end_for[dir]
            temp_set = set()
            if dir == 0 or dir == 1:
                for i in range(s, e):
                    if (i, loc_of_core[1]) not in visited_loc:
                        temp_set.add((i, loc_of_core[1]))            
            else:
                for j in range(s, e):
                    if (loc_of_core[0], j) not in visited_loc:
                        temp_set.add((loc_of_core[0], j))            
            if len(temp_set) == e - s: 
                solution(visited_loc | temp_set, loc_of_cores, circuit, target_core_idx+1, 
                        num_of_linked_lines+(e-s), num_of_linked_cores+1)


T = int(input())

for t_iter in range(1, T+1):
    max_cores = -1
    min_lines = float('inf')

    N = int(input())

    loc_of_cores = {}   # key: core index, value: core location (tuple)
    core_idx = 0
    circuit = []

    visited_set = set()
    for n_iter in range(N):
        line = list(map(int, input().split())) 
        for idx, val in enumerate(line):
            if val == 1:
                visited_set.add((n_iter, idx))
                if n_iter == 0 or n_iter == N - 1:  # 가장자리에 있을 경우에는 전선을 따로 연결하지 않아도 됨.
                    line[idx] = 2
                elif idx == 0 or idx == N - 1:      # 가장자리에 있을 경우에는 전선을 따로 연결하지 않아도 됨.
                    line[idx] = 2
                else:                               # 가장자리가 아닌 어딘가에 있는 코어는 전선을 달아줘야 함.
                    loc_of_cores[core_idx] = (n_iter, idx, )
                    core_idx += 1
        circuit.append(line)

    solution(visited_set, loc_of_cores, circuit, 0, 0, 0)

    print(f"#{t_iter} {min_lines}")