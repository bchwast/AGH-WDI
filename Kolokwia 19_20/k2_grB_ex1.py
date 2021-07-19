def to_7sys(n):
    c_n = n
    l = 0
    while c_n > 0:
        l += 1
        c_n //= 7

    num = [0]*l

    for i in range(l-1, -1, -1):
        num[i] = n%7
        n //= 7

    return num
#end def


def ile_niep(num):
    ilosc = 0
    for i in range(len(num)):
        if num[i]%2 == 1:
            ilosc += 1
    return ilosc
#end def


def zgodne(n1, n2):
    num1 = to_7sys(n1)
    num2 = to_7sys(n2)
    return ile_niep(num1) == ile_niep(num2)
#end def


def matrioszka(tab1, tab2):
    n1 = len(tab1)
    n2 = len(tab2)
    for w2 in range(n2-n1):
        for k2 in range(n2-n1):
            ilosc = 0
            for w1 in range(n1):
                for k1 in range(n1):
                    if zgodne(tab1[w1][k1], tab2[w2+w1][k2+k1]):
                        ilosc += 1
                #end for
            #end for
            if ilosc >= (n1*n1)/3:
                return True
        #end for
    #end for
    return False
#end def

t1 = [[2 for _ in range(3)] for _ in range(3)]
t2 = [[2 for _ in range(10)] for _ in range(10)]
print(matrioszka(t1, t2))
