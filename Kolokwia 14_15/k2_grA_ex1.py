def odl(krol):
    w = krol[0]
    k = krol[1]
    ruchy = 0
    while w != 101 and k != 101:
        if w < 101:
            w += 1
        else:
            w -= 1

        if k < 101:
            k += 1
        else:
            k -= 1

        ruchy += 1
    #end while
    if w == 101:
        ruchy += abs(101-k)
    elif k == 101:
        ruchy += abs(101-w)

    return ruchy
#end def

def krole(pos):
    for i in range(100):
        for j in range(100):
            if i != j:
                if odl(pos[i]) == odl(pos[j]):
                    return pos[i], pos[j]
        #end for
    #end for
    return False
#end def

pozycje = [None]*100
i = 0
while i < 100:
    w = int(input("wiersz: "))
    k = int(input("kolumna: "))
    pozycje[i] = w,k
    i += 1
#end while

wynik = krole(pozycje)
if wynik:
    print(f"wiersz: {wynik[0]}, kolumna: {wynik[1]}")
else:
    print("Brak pary krolow rownoodleglej od srodka")