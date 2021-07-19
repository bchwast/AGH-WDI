from random import randint

def sortuj(tab):
    sortowac = True
    while sortowac:
        sortowac = False
        for i in range(M-1):
            if tab[i+1] < tab[i]:
                sortowac = True
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
    return tab


def przepis(tab1, tab2):
    a = 0
    for i in range(N):
        for j in range(N):
            tab2[a] = tab1[i][j]
            a += 1
    tab2 = sortuj(tab2)
    return tab2


N = int(input("> "))
T1 =[]
for i in range(N):
    T1.append([])
    for _ in range(N):
        T1[i].append(1)
for i in range(N):
    for j in range(N-1):
        T1[i][j+1] = T1[i][j] + randint(0,10)
M = N*N
T2 = [0 for _ in range(M)]
print(T1)
print(przepis(T1,T2))