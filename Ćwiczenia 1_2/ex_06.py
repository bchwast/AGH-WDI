eps = 0.00000000001

a = -99
b = 99

while True:
    c = (a+b)/2
    if abs(b-c) <= eps:
        print(c)
        break
    if (b**b - 2020)*(c**c - 2020) <= 0:
        a = c
    else:
        b = c