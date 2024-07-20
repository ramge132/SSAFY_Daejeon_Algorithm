N = int(input())

S_n = []
E_n = []
for n_iter in range(N):
    s, e = map(int, input().split())
    S_n.append(s)
    E_n.append(e)

meeting_count = 0
sorted_idx_of_E_n = sorted(range(len(E_n)), key=lambda k: (E_n[k], S_n[k]))

previous_end_time = -1
for idx in sorted_idx_of_E_n:
    if S_n[idx] >= previous_end_time:
        meeting_count = meeting_count + 1
        previous_end_time = E_n[idx]

print(meeting_count)