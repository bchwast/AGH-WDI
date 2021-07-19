def wypisz(t):
    n = len(t)
    for i in range(n):
        print("[",end="")
        for j in range(n-1):
            if t[i][j] < 10:
                print(f"0{t[i][j]}|",end="")
            else:
                print(f"{t[i][j]}|",end="")
        if t[i][n-1] < 10:
            print(f"0{t[i][n-1]}]")
        else:
            print(f"{t[i][n-1]}]")
    print("")
    #end for
#end def


def ruchy(T, mode, w, k):
    wiersze = [-2, -1, 1, 2, 2, 1, -1, -2]
    kolumny = [1, 2, 2, 1, -1, -2, -2, -1]
    w += wiersze[mode]
    k += kolumny[mode]
    if w >= 0 and w < len(T) and k >= 0 and k < len(T) and T[w][k] == 0:
        return (w, k)
    return None


def skoczek(T, w=0, k=0, ruch=1):
    T[w][k] = ruch
    if ruch == len(T)**2:
        wypisz(T)
        exit(0)
    for mode in range(0,8):
        skok = ruchy(T, mode, w, k)
        if skok is not None:
            skoczek(T, skok[0], skok[1], ruch+1)
    #end for
    T[w][k] = 0


t = [[0 for _ in range(5)] for _ in range(5)]
skoczek(t)