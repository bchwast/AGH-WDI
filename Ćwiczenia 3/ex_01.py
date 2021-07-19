def fibo(x):
    f1 = 1
    f2 = 1
    g1 = 1
    g2 = 1
    while g1 <= x:
        while f1 <= x:
            if f1*g1 == x:
                return True
            f1 = f1 + f2
            f2 = f1 - f2
        g1 = g1 + g2
        g2 = g1 - g2
        f1 = 1
        f2 = 1
    return False


y = int(input("> "))

if fibo(y) == True: print("tak")
else: print("nie")
