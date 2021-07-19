# Bartłomiej Chwast
# Zadanie 3. 3 funkcje pomocnicze: funkcja sumująca liczby w kolumnach, sumująca liczby w wierszach, sumująca liczby na polach szachowanych. tworzymy tablice z sumami liczb w wierszach i kolumnach, sprawdzamy petlą zagnieżdżoną dla każdego ustawienia wież, gdy nie są one na jednym polu. zakładam minimalną sumę liczb na szachownicy: -99999999999999999

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


def chess(t):
    def sumasz(tab, w1, k1, w2, k2):
        szach = suma_w[w1] + suma_w[w2] + suma_k[k1] + suma_k[k2]
        szach -= 2*(tab[w1][k1] + tab[w2][k2])

        if w1 == w2:
            szach -= suma_w[w2]
        elif k1 == k2:
            szach -= suma_k[k2]
        else:
            szach -= (tab[w1][k2] + tab[w2][k1])

        return szach
    #end def


    row1 = col1 = row2 = col2 = 0
    suma_m = -99999999999999999
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
                        #end if
                #end for
            #end for
        #end for
    #end for
    return (row1, col1, row2, col2)
#end def
