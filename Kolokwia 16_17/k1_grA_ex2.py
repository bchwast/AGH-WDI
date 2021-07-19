from random import randint


def s_max(tab):
    MAX = len(tab)
    suma = 0
    lrgst = 0
    lrgst_prev = 1001

    for _ in range(10):
        for i in range(MAX):
            if tab[i] > lrgst and tab[i] < lrgst_prev:
                lrgst = tab[i]
            #end if
        #end for
        suma += lrgst
        lrgst_prev = lrgst
        lrgst = 0
    #end for

    return suma
#end def


tab = [randint(1,1000) for _ in range(100)]
print(s_max(tab))
