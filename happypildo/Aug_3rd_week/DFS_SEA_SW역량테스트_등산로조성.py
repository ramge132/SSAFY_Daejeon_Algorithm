from copy import deepcopy

DIRECTION = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_peaks(temp_peak_info):
    keys = list(temp_peak_info.keys())
    peak = max(keys)

    return peak


longest_path_length = -1
def modified_DFS(N, mountain, current_point, path_length):    
    global longest_path_length

    i, j = current_point
    for direction in DIRECTION:
        temp_i = i + direction[0]
        temp_j = j + direction[1]

        if (-1 < temp_i < N) and (-1 < temp_j < N):
            if (mountain[temp_i][temp_j] < mountain[i][j]) and (temp_i, temp_j):
                modified_DFS(N, mountain, (temp_i, temp_j), path_length+1)

    if longest_path_length < path_length:
        longest_path_length = path_length


def solve(N, K, mountain, peaks):
    global longest_path_length
    longest_path_length = -1

    for i in range(N):
        for j in range(N):
            for depth in range(K + 1):
                temp_peaks = deepcopy(peaks)
                temp_map = deepcopy(mountain)

                origin_idx = temp_peaks[temp_map[i][j]].index((i, j))
                del temp_peaks[temp_map[i][j]][origin_idx]

                key = temp_map[i][j] - depth
                value = temp_peaks.get(key, None)
                if value is None:
                    temp_peaks[key] = [(i, j)]
                else:
                    temp_peaks[key].append((i, j))
                
                temp_map[i][j] -= depth
                to_search_peaks = temp_peaks[get_peaks(temp_peaks)]
                
                for p in to_search_peaks:
                    modified_DFS(N, temp_map, p, 0)


T = int(input())
for t_iter in range(1, T+1):
    N, K = list(map(int, input().split()))

    input_map = []
    peak_info = {}
    for n_iter in range(N):
        input_line = list(map(int, input().split()))
        input_map.append(input_line)
        for i, h in enumerate(input_line):
            key = h
            value = peak_info.get(key, None)
            if value is None:
                peak_info[key] = [(n_iter, i)]
            else:
                peak_info[key].append((n_iter, i))

    solve(N, K, input_map, peak_info)
    print(f"#{t_iter} {longest_path_length + 1}")