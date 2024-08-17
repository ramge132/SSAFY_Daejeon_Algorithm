N = int(input())

strengths = []
for n_iter in range(N):
    strength = int(input())
    strengths.append(strength)

sorted_strengths = sorted(strengths)
possible_weight = [s * w for s, w in zip(sorted_strengths, range(N, -1, -1))]

print(max(possible_weight))