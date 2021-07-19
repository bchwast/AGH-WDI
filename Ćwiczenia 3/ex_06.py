x = int(input("> "))

dif = x - 1
a = 1
while a < x/2:
    if x%a == 0:
        b = x//a
        if abs(a - b) < dif:
            dif = abs(a-b)
            f_a = a
            f_b = b
    if dif <= 1: break
    a += 1

print(f_a,f_b)