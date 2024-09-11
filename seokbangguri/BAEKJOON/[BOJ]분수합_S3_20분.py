def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lessgo(a, b):
    huge = gcd(a, b)
    a = a // huge
    b = b // huge
    
    return a, b

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a, b = a1*b2 + a2*b1, b1*b2
a, b = lessgo(a, b)
print(a, b)