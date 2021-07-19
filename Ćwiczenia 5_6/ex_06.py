from random import randint


def sortuj(tab):
    sortowac = True
    while sortowac:
        sortowac = False
        for i in range(M-1):
            if tab[i+1] < tab[i] and tab[i+1] != 0 and tab[i] != 0:
                sortowac = True
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
    return tab


def singletony(tab1, tab2):
    wynik = tab2
    ind = 0
    for i in range(N):
        for j in range(N):
            komorka = tab1[i][j]
            sprawdz = True
            for a in range(N):
                for b in range(N):
                    if i == a and j == b:
                        continue
                    if komorka >= tab1[a][b]:
                        if komorka == tab1[a][b]:
                            sprawdz = False
                            break
                    else:
                        break
                if not sprawdz:
                    break
            if sprawdz:
                wynik[ind] = komorka
                ind += 1
    wynik = sortuj(wynik)
    return wynik


N = int(input("> "))
T1 = []
for i in range(N):
    T1.append([])
    for _ in range(N):
        T1[i].append(1)
for i in range(N):
    for j in range(N-1):
        T1[i][j+1] = T1[i][j] + randint(1,11)
M = N*N
T2 = [0]*(M)

print(T1)
print(singletony(T1,T2))