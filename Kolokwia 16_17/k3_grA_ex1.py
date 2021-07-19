def do_tablicy(num):
    c_num = num
    l = 0
    while c_num > 0:
        l += 1
        c_num //= 10

    n = [0]*l

    for i in range(l-1, -1, -1):
        n[i] = num%10
        num //= 10

    return n
#end def


def czy_kolezanki(n1, n2):
    num1 = do_tablicy(n1)
    num2 = do_tablicy(n2)

    licznik = 0
    a = -1
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i] == num2[j]:
                if a != num1[i]:
                    licznik += 1
            #end if
        #end for
    #end for

    if licznik >= 2:
        return True
    return False
#end def


def kolezanki(t):
    zerowane = 0
    n = len(t)

    for w1 in range(n):
        for k1 in range(n):
            num1 = t[w1][k1]
            ma = False
            for w2 in range(n):
                if ma:
                    break
                for k2 in range(n):
                    if w1 != w2 or k1 != k2:
                        if czy_kolezanki(num1, t[w2][k2]):
                            ma = True
                            break
                #end for
            #end for
            if not ma:
                zerowane += 1
        #end for
    #end for

    return (n*n) - zerowane
#end def


