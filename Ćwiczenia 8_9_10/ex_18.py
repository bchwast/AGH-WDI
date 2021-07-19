from random import randint


fin = False
def krol(plansza, w, k, kontrola, r=1):
    global fin
    kontrola[w][k] = r
    if w == k == 7:
        fin = True
        return True
    else:
        for i in range(0, 5):
            if i == 0 and k < 7 and w > 0 and plansza[w][k]%10 < int(str(plansza[w-1][k+1])[0]) and kontrola[w-1][k+1] == 0:
                if krol(plansza, w-1, k+1, kontrola, r+1):
                    return True
            if i == 1 and k < 7 and plansza[w][k]%10 < int(str(plansza[w][k+1])[0]) and kontrola[w][k+1] == 0:
                if krol(plansza, w, k+1, kontrola, r+1):
                    return True
            if i == 2 and k < 7 and w < 7 and plansza[w][k]%10 < int(str(plansza[w+1][k+1])[0]) and kontrola[w+1][k+1] == 0:
                if krol(plansza, w+1, k+1, kontrola, r+1):
                    return True
            if i == 3 and w < 7 and plansza[w][k]%10 < int(str(plansza[w+1][k])[0]) and kontrola[w+1][k] == 0:
                if krol(plansza, w+1, k, kontrola, r+1):
                    return True
            if i == 4 and w < 7 and k > 0 and plansza[w][k]%10 < int(str(plansza[w+1][k-1])[0]) and kontrola[w+1][k-1] == 0:
                if krol(plansza, w+1, k-1, kontrola, r+1):
                    return True
        if not fin:
            kontrola[w][k] = 0
            return False
#end def


t = [[randint(1,99999) for _ in range(8)] for _ in range(8)]
kontrola = [[0 for _ in range(8)] for _ in range(8)]
print(krol(t, 0, 0, kontrola))

