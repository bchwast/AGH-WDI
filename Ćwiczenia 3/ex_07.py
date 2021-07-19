def ser_a(n):
    return n*n+n+1


def check(a):
    i = 1
    while a >= ser_a(i):
        k = 1
        while a >= k*ser_a(i):
            if a%(k*ser_a(i)) == 0: return True
            else: k += 1
        i += 1
    return False


x = int(input("> "))
if check(x) == True: print("tak")
else: print("nie")
