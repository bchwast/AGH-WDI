def suma_fib(num):
    f1 = 1
    f2 = 1
    while f1 <= num//2 + 1:
        a1 = f1
        a2 = f2
        sum = 0
        while sum <= num:
            if sum == num:
                return True
            sum += a1
            temp = a1
            a1 = a2
            a2 += temp
        #end while
        temp = f1
        f1 = f2
        f2 += temp

    #end while
    return False
#end def


def nastepna(n):
    num = n+1
    while suma_fib(num):
        num += 1
    return num
#end def


n = int(input("> "))
print(nastepna(n))
