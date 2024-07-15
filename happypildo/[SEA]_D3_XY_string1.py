def recurssive_E(S, E):
    if E == S:
        return "Yes";
    if len(E) == len(S):
        return "No";
    ret = ""

    # For type 1 transformation
    if E[-1] == 'X':
        ret = ret + recurssive_E(S, E[:-1])
        return ret
    
    if E[::-1][0] == 'Y':
        ret = ret + recurssive_E(S, E[::-1][1:])
        return ret
    
# print(recurssive_E("YY", "XYYX"))
T = int(input())
for t_iter in range(1, T+1):
    S = input()
    E = input()

    print(recurssive_E(S, E))