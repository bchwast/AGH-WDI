def fibo(target):
    a = 1
    b = 1
    sum = b
    end = False

    while end == False:
        while sum <= target:
            f1 = a
            f2 = b
            while sum <= target:
                if sum == target:
                    end = True
                    break
                else:
                    sum = sum + f1
                    f1 = f1 + f2
                    f2 = f1 - f2
            if end == True:
                break
            a = a + b
            b = a - b
            sum = b
        target += 1

    return target


n = int(input("> "))
print(fibo(n))