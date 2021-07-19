from math import inf


def A(x):
    return x + 3
#end def


def B(x):
    return 2*x
#end def


def to_tab(n):
    c_n = n
    l = 0
    while c_n > 0:
        l += 1
        c_n //= 10

    num = [0]*l
    for i in range(l-1, -1, -1):
        num[i] = n%10
        n //= 10

    return num
#end def


def C(n):
    num = to_tab(n)
    for i in range(len(num)):
        if num[i]%2 == 1:
            num[i] -= 1

    x = 0
    ind = 0
    for i in range(len(num)-1, -1, -1):
        x += num[i]*(10**ind)
        ind += 1

    return x
#end def


def przemiana(x, y, n):
    licznik = inf

    def przek(x, y, n, steps=0, last=0):
        nonlocal licznik
        if n == -1:
            return False

        if x == y:
            licznik = min(licznik, steps)
            return True

        if last != 1:
            przek(A(x), y, n-1, steps+1, 1)
        if last != 2:
            przek(B(x), y, n-1, steps+1, 2)
        if last != 3:
            przek(C(x), y, n-1, steps+1, 3)
    #end def

    przek(x, y, n)
    if licznik == inf:
        return -1
    return licznik
#end def


print(przemiana(23, 27, 5))


