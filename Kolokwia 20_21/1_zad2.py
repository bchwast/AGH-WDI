# Bartłomiej Chwast
# program zamienia liczbe na dziesietna, sprawdza roznice, jak wiersze sa pod soba to odleglosc wynosi 0

def zamiana_podstaw(liczba):
    new_liczba = 0
    N = len(liczba)
    for i in range(N):
        new_liczba += (liczba[i]%2)*(2**i)
    #end for
    return new_liczba
#end def


def distance(T):
    N = len(T)
    diff_m = 0
    for i in range(N):
        liczba1 = zamiana_podstaw(T[i])
        for j in range(N):
            if i != j:
                liczba2 = zamiana_podstaw(T[j])
                diff = abs(liczba1 - liczba2)
                if diff > diff_m:
                    odl = abs(i-j) - 1
                #end if
            #end if
        #end for
    #end for
    return odl
#end def

