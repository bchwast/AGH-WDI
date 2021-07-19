x = float(input("> "))

eps = 0.00000001
a = 1
b = x

while abs(a - b) >= eps:
    a = (a+b)/2
    b = x/a

print(a)

