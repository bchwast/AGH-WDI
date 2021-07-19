from random import randint


fin = False
def krol(plansza, w, k, kontrola, r, droga):
    global fin
    kontrola[w][k] = r
    if w == k == 0 or (w == 0 and k == 7) or (w == 7 and k == 7) or w == k == 7:
        fin = True
        return True
    else:
        for i in range(0, 8):
            if i == 0 and k < 7 and w > 0 and plansza[w][k]%10 < int(str(plansza[w-1][k+1])[0]) and kontrola[w-1][k+1] == 0:
                droga[r-1] = i
                if krol(plansza, w-1, k+1, kontrola, r+1, droga):
                    return True
            if i == 1 and k < 7 and plansza[w][k]%10 < int(str(plansza[w][k+1])[0]) and kontrola[w][k+1] == 0:
                droga[r-1] = i
                if krol(plansza, w, k+1, kontrola, r+1, droga):
                    return True
            if i == 2 and k < 7 and w < 7 and plansza[w][k]%10 < int(str(plansza[w+1][k+1])[0]) and kontrola[w+1][k+1] == 0:
                droga[r-1] = i
                if krol(plansza, w+1, k+1, kontrola, r+1, droga):
                    return True
            if i == 3 and w < 7 and plansza[w][k]%10 < int(str(plansza[w+1][k])[0]) and kontrola[w+1][k] == 0:
                droga[r-1] = i
                if krol(plansza, w+1, k, kontrola, r+1, droga):
                    return True
            if i == 4 and w < 7 and k > 0 and plansza[w][k]%10 < int(str(plansza[w+1][k-1])[0]) and kontrola[w+1][k-1] == 0:
                droga[r-1] = i
                if krol(plansza, w+1, k-1, kontrola, r+1, droga):
                    return True
            if i == 5 and k > 0 and plansza[w][k]%10 < int(str(plansza[w][k-1])[0]) and kontrola[w][k-1] == 0:
                droga[r-1] = i
                if krol(plansza, w, k-1, kontrola, r+1, droga):
                    return True
            if i == 6 and k > 0 and w > 0 and plansza[w][k]%10 < int(str(plansza[w-1][k-1])[0]) and kontrola[w-1][k-1] == 0:
                droga[r-1] = i
                if krol(plansza, w-1, k-1, kontrola, r+1, droga):
                    return True
            if i == 7 and w > 0 and plansza[w][k]%10 < int(str(plansza[w-1][k])[0]) and kontrola[w-1][k] == 0:
                droga[r-1] = i
                if krol(plansza, w-1, k, kontrola, r+1, droga):
                    return True
        if not fin:
            kontrola[w][k] = 0
            droga[r-1] = None
            return False
#end def


t = [[randint(1,99999) for _ in range(8)] for _ in range(8)]
kontrola = [[0 for _ in range(8)] for _ in range(8)]
droga = [None]*64
krol(t, 4, 6, kontrola, 1, droga)
for i in range(len(droga)):
    if droga[i] != None:
        print(droga[i], end=" ")
#end for

