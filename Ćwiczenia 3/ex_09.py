k = int(input("> "))

eps = 10000000
dx = k/eps
x = 2
P = 0

while x < k:
    p = dx*(1/x)
    x = x + dx
    P += p

print(P)
