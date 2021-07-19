x = float(input("> "))

eps = 0.0000000000001
a = 1
b = 1
c = x

while abs(a - c) >= eps:
    a = (a+b+c)/3
    b = a
    c = x/(a*b)

print(a)

