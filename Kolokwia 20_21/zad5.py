# Bartłomiej Chwast
# Wyniki testów są niezgodne z poleceniem, dlatego przygotowałem dwie wersje zadania
# Pierwsza (zgodna z testami) liczy nwd każdej pary liczb w trójce i to nwd ma być za każdym razem równe 1, wszystko w
# pętlach for z zabezpieczeniem wyjścia z tablicy
# Druga (zgodna z poleceniem) liczy nwd całej trójki, ma być ono równe 0, reszta tak samo jak w pierwszej wersji

def nwd(a, b):
    while b != 0:
        b, a = a%b, b
    #end while
    return a
#end def

def trojki(T):
    N = len(T)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, i+3, 1):
            if j < N:
                for k in range(j+1, j+3, 1):
                    if k < N and nwd(T[i],T[j]) == nwd(T[j],T[k]) == nwd(T[i],T[k]) == 1:
                        cnt += 1
                #end for
        #end for
    #end for
    return cnt
#end def


"""
def trojki(T):
    N = len(T)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1, i+3, 1):
            if j < N:
                for k in range(j+1, j+3, 1):
                    if k < N and nwd(nwd(T[i], T[j]), T[k]) == 1:
                        cnt += 1
                #end for
        #end for
    #end for
    return cnt
#end def
"""


