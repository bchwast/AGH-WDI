def eq(x, y):

    for i in range(2, 17):
        x_c = x
        y_c = y
        x_n = y_n = 0
        p = 0
        while x_c > 0:
            x_n += (x_c%i)*(10**p)
            if x_c%1 > 9:
                p += 1
            x_c //= i
            p += 1
        p = 0
        while y_c > 0:
            y_n += (y_c%i)*(10**p)
            if y_c%i > 9:
                p += 1
            y_c //= i
            p += 1

        x_c = x_n
        no = False
        while x_c > 0:
            d = x_c%10
            y_c = y_n
            while y_c > 0:
                e = y_c%10
                if d == e:
                    no = True
                    break
                y_c //= 10
            if no == True:
                break
            x_c //= 10
        if no == False:
            return i

    return 0


a = int(input("> "))
b = int(input("> "))

res = eq(a,b)
if res == 0:
    print("nie ma takiej podstawy")
else:
    p = a_n = 0
    while a > 0:
        a_n += (a % res) * (10 ** p)
        if a % 1 > 9:
            p += 1
        a //= res
        p += 1
    p = b_n = 0
    while b > 0:
        b_n += (b % res) * (10 ** p)
        if b % res > 9:
            p += 1
        b //= res
        p += 1
    print(f"podstawa to {res}, a liczby to {a_n} i {b_n} ")
