a0 = 0
a1 = 1
b0 = 2
a2 = a1 - (b0*a0)
b1 = b0 + (2*a1)

while int(input("> ")) == a0:
    print(b0)
    a0, a1, b0, a2, b1 = a1, a2, b1, a2 - (b1*a1), b1 + (2*a2)
    