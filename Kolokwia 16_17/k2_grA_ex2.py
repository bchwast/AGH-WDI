def sumak(t, k):
    suma = 0
    for i in range(len(t)):
        suma += t[i][k]
    return suma
#end def


def sumaw(t, w):
    suma = 0
    for i in range(len(t)):
        suma += t[w][i]
    return suma
#end def


def sumasz(t, w1, k1, w2, k2, suma_w, suma_k):
    suma = suma_w[w1] + suma_w[w2] + suma_k[k1] + suma_k[k2]
    suma -= 2*(t[w1][k1] + t[w2][k2])

    if w1 == w2:
        suma -= suma_w[w2]
    elif k1 == k2:
        suma -= suma_k[k2]
    else:
        suma -= (t[w1][k2] + t[w2][k1])

    return suma
#end def


def wieze(t):
    w1 = w2 = k1 = k2 = 0
    suma_m = 0
    n = len(t)
    suma_w = [sumaw(t, w) for w in range(n)]
    suma_k = [sumak(t, k) for k in range(n)]

    for r1 in range(n):
        for c1 in range(n):
            for r2 in range(n):
                for c2 in range(n):
                    if c1 != c2 and r1 != r2:
                        suma = sumasz(t, r1, c1, r2, c2, suma_w, suma_k)
                        if suma > suma_m:
                            suma_m = suma
                            w1 = r1
                            w2 = r2
                            k1 = c1
                            k2 = c2
                    #end if
                #end for
            #end for
        #end for
    #end for

    return ((w1, k1), (w2, k2))
#end def


t = [[0, 20, 0, 0, 0, 0],[20, 20, 20, 20, 20, 20],[0, 20, 0 ,0 ,0 ,0],[0, 20, 0, 0, 0, 0],[0, 20, 0, 0, 0, 0],[0, 20, 0, 0, 0 ,0]]
print(wieze(t))


