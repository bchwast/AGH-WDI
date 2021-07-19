a = 0
b = 1
t1 = 2020
t2 = 2020

while a <= 1010:
    for b in range(1,1012,1):
        if a < b:
            continue
        else:
            f1 = a
            f2 = b
            while f1 <= 2020:
                if (f1 == 2020 or f2 == 2020) and a + b < t1 + t2:
                    t1 = a
                    t2 = b
                f1 = f1 + f2
                f2 = f1 - f2
    a += 1

print(t2, t1)