def sumyk(t, k):
    suma = 0
    for i in range(len(t)):
        suma += t[i][k]
    return suma
#end def


def sumyw(t, w):
    suma = 0
    for i in range(len(t)):
        suma += t[w][i]
    return suma
#end def


def sumasz(t, w1, k1, w2, k2, sumy_k, sumy_w):
    suma = sumy_k[k1] + sumy_k[k2] + sumy_w[w1] + sumy_w[w2]
    suma -= (2*t[w1][k1] + 2*t[w2][k2])
    if w1 == w2:
        suma -= sumy_w[w2]
    elif k1 == k2:
        suma -= sumy_k[k2]
    else:
        suma -= (t[w1][k2] + t[w2][k1])
    return suma
#end def


def wieze(t, w1, k1, w2, k2):
    n = len(t)
    sumy_k = [sumyk(t, k) for k in range(n)]
    sumy_w = [sumyw(t, w) for w in range(n)]
    suma = sumasz(t, w1, k1, w2, k2, sumy_k, sumy_w)

    for i in range(n):
        if k1 != k2:
            if sumasz(t, i, k1, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if sumasz(t, w1, k1, i, k2, sumy_k, sumy_w) > suma:
                return True
        if k1 == k2 and w1 < w2:
            if i < w2 and sumasz(t, i, k1, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if i > w1 and sumasz(t, w1, k1, i, k2, sumy_k, sumy_w) > suma:
                return True
        if k1 == k2 and w1 > w2:
            if i > w2 and sumasz(t, i, k1, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if i < w1 and sumasz(t, w1, k1, i, k2, sumy_k, sumy_w) > suma:
                return True

        if w1 != w2:
            if sumasz(t, w1, i, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if sumasz(t, w1, k1, w2, i, sumy_k, sumy_w) > suma:
                return True
        if w1 == w2 and k1 < k2:
            if i < k2 and sumasz(t, w1, i, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if i > k1 and sumasz(t, w1, k1, w2, i, sumy_k, sumy_w) > suma:
                return True
        if w1 == w2 and k1 > k2:
            if i > k2 and sumasz(t, w1, i, w2, k2, sumy_k, sumy_w) > suma:
                return True
            if i < k1 and sumasz(t, w1, k1, w2, i, sumy_k, sumy_w) > suma:
                return True
    #end for
    return False
#end def
