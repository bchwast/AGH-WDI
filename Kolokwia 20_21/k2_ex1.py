# 5 pkt

def sumak(t, k):
    suma = 0
    for i in range(len(t)):
        suma += t[i][k]
    return suma


def sumaw(t, w):
    suma = 0
    for i in range(len(t)):
        suma += t[w][i]
    return suma


def chess(t):
    def sumasz(tab, w1, k1, w2, k2):
        szach = suma_w[w1] + suma_w[w2] + suma_k[k1] + suma_k[k2]
        szach -= 2 * (tab[w1][k1] + tab[w2][k2])

        if w1 == w2:
            szach -= suma_w[w2]
        elif k1 == k2:
            szach -= suma_k[k2]
        else:
            szach -= (tab[w1][k2] + tab[w2][k1])

        return szach


    row1 = col1 = row2 = col2 = 0
    suma_m = float("-inf")
    n = len(t)
    suma_w = [sumaw(t, w) for w in range(n)]
    suma_k = [sumak(t, k) for k in range(n)]

    for r1 in range(n):
        for c1 in range(n):
            for r2 in range(n):
                for c2 in range(n):
                    if c1 != c2 or r1 != r2:
                        suma = sumasz(t, r1, c1, r2, c2)
                        if suma > suma_m:
                            suma_m = suma
                            row1 = r1
                            col1 = c1
                            row2 = r2
                            col2 = c2

    return (row1, col1, row2, col2)
