def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 or num%3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
        if num%i == 0:
            return False
        i += 4

    return True
#end def


def uklad(t, mode, w1 ,k1):
    poz_w = [-2, -1, 1, 2, 2, 1, -1, -2]
    poz_k = [1, 2, 2, 1, -1, -2, -2, -1]
    w2 = w1 + poz_w[mode]
    k2 = k1 + poz_k[mode]
    if w2 < 0 or k2 < 0 or w2 >= len(t) or k2 >= len(t):
        return False
    suma = t[w1][k1] + t[w2][k2]
    if prime(suma):
        return True
    return False
#end def


def skoczki(t):
    n = len(t)
    for w1 in range(n):
        for k1 in range(n):
            for mode in range(8):
                if uklad(t, mode, w1, k1):
                    return True
            #end for
        #end for
    #end for
    return False
#end def

