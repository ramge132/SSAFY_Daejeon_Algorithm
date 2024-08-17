T = int(input())

# Make DP table
ABSOLUTE_NUM = 30       # Problem definition
DP_table = [
        [0 for m_iter in range(ABSOLUTE_NUM + 1)] 
        for n_iter in range(ABSOLUTE_NUM + 1)
    ]

## DP Initialization
for m_iter in range(1, ABSOLUTE_NUM + 1):
    DP_table[1][m_iter] = m_iter

for n_iter in range(2, ABSOLUTE_NUM + 1):
    interest_list = DP_table[n_iter - 1]
    for m_iter in range(2, ABSOLUTE_NUM + 1):
        DP_table[n_iter][m_iter] = sum(interest_list[:m_iter])

for t_iter in range(T):
    N, M = map(int, input().split())

    print(DP_table[N][M])
