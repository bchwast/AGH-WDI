def do_tablicy(n):
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


def czy_przyjaciolki(n1, n2):
    num1 = do_tablicy(n1)
    num2 = do_tablicy(n2)

    for i in range(len(num1)):
        okay = False
        for j in range(len(num2)):
            if num1[i] == num2[j]:
                okay = True
                break
        #end for
        if not okay:
            return False
    #end for
    for i in range(len(num2)):
        okay = False
        for j in range(len(num1)):
            if num2[i] == num1[j]:
                okay = True
                break
        #end for
        if not okay:
            return False
    #end for
    return True
#end def


def przyjaciolki(t):
    n = len(t)
    ilosc = 0
    for w in range(n):
        for k in range(n):
            num = t[w][k]
            if w > 0:
                if not czy_przyjaciolki(num, t[w-1][k]):
                   continue
            if w < n-1:
                if not czy_przyjaciolki(num, t[w+1][k]):
                    continue
            if k > 0:
                if not czy_przyjaciolki(num, t[w][k-1]):
                    continue
            if k < n-1:
                if not czy_przyjaciolki(num, t[w][k+1]):
                    continue
            ilosc += 1
        #end for
    #end for
    return ilosc
#end def

