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

def wieze(t, w1, k1, w2, k2):
    def sumasz(r1, c1, r2, c2):
        s = sumy_k[c1] + sumy_k[c2] + sumy_w[r1] + sumy_w[r2]
        s -= (2*t[r1][c1] + 2*t[r2][c2])
        if r1 == r2:
            s -= sumy_w[r2]
        elif c1 == c2:
            s -= sumy_k[c2]
        else:
            s -= (t[r1][c2] + t[r2][c1])
        return s
    #end def

    n = len(t)
    sumy_k = [sumyk(t, k) for k in range(n)]
    sumy_w = [sumyw(t, w) for w in range(n)]
    suma = sumasz(w1, k1, w2, k2)

    for i in range(n):
        #ruch po w1
        if w1 != w2 or (w1 == w2 and i != k2):
            if sumasz(w1, i, w2, k2) > suma:
                return True
        #ruch po w2
        if w2 != w1 or (w2 == w1 and i != k1):
            if sumasz(w1, k1, w2, i) > suma:
                return True
        #rucn po k1
        if k1 != k2 or (k1 == k2 and i != w2):
            if sumasz(i, k1, w2, k2) > suma:
                return True
        #ruch po k2
        if k2 != k1 or (k2 == k1 and i != w1):
            if sumasz(w1, k1, i, k2) > suma:
                return True
    #end for
    return False
#end def




