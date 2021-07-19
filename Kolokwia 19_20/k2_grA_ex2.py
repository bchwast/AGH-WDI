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


def C(x):
    num = to_tab(x)
    for i in range(len(num)):
        if num[i]%2 == 0:
            num[i] += 1

    res = 0
    wyk = 0
    for i in range(len(num)-1, -1, -1):
        res += num[i]*(10**wyk)
        wyk += 1

    return res
#end def

def przeksztalcenie(x, y, n):
    licznik = 0

    def przem(x, y, n, last=0):
        nonlocal licznik
        if n == -1:
            return False

        if x == y:
            licznik += 1
            return

        if last != 1:
            przem(A(x), y, n-1, 1)
        if last != 2:
            przem(B(x), y, n-1, 2)
        if last != 3:
            przem(C(x), y, n-1, 3)
    #end def

    przem(x, y, n)
    return licznik
#end def


print(przeksztalcenie(11, 31, 4))