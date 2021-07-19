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


def znajdz_wolne(plansza):
    for w in range(9):
        for k in range(9):
            if plansza[w][k] == 0:
                return (w, k)
    #end for
    return None
#end def


def moze(plansza, cyfra, w, k):
    for i in range(9):
        if plansza[w][i] == cyfra and i != k:
            return False
        if plansza[i][k] == cyfra and i != w:
            return False
    #end for

    kwadrat_w = w // 3
    kwadrat_k = k // 3

    for i in range(kwadrat_w*3, kwadrat_w*3 + 3):
        for j in range(kwadrat_k*3, kwadrat_k*3 + 3):
            if plansza[i][j] == cyfra and i != w and j != k:
                return False
    #end for
    return True
#end def


def sudoku(plansza):
    wolne = znajdz_wolne(plansza)
    if wolne is None:
        return True
    w, k = wolne

    for cyfra in range(1, 10):
        if moze(plansza, cyfra, w, k):
            plansza[w][k] = cyfra

            if sudoku(plansza):
                return True

            plansza[w][k] = 0
    #end for
    return False
#end def


plansza = [[0 for _ in range(9)] for _ in range(9)]
sudoku(plansza)
wypisz(plansza)