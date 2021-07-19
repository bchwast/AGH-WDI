def podzielniki(num, podz):
    ind = 0
    i = 2
    while num > 1:
        if num%i == 0:
            podz[ind] = i
            ind += 1
            while num%i == 0:
                num //= i
        i += 1
    return ind
#end def


def core(podz, n, iloczyn=1, ind=0):
    if ind == n:
        if iloczyn != 1:
            return iloczyn
        return 0
    wynik = 0
    wynik += core(podz, n, iloczyn, ind+1)
    iloczyn *= podz[ind]
    wynik += core(podz, n, iloczyn, ind+1)
    return wynik
#end def


def suma(num):
    podz = [None]*20
    n = podzielniki(num, podz)
    return core(podz, n)
#end def


print(suma(60))

