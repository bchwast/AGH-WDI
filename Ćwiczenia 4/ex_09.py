from random import randint

def sortuj(tab):
    sortowac = True
    while sortowac == True:
        sortowac = False
        for i in range(len(tab)-1):
            if tab[i+1] > tab[i]:
                sortowac = True
                temp = tab[i]
                tab[i] = tab[i+1]
                tab[i+1] = temp
    return tab

def podciag(tab):
    pdcg = [1 for _ in range(N)]
    a = 0
    for i in range(0,len(tab)-1):
        if tab[i+1] > tab[i]:
            pdcg[a] += 1
        else:
            a += 1
    pdcg = sortuj(pdcg)
    return pdcg[0]


N = int(input("> "))
t = [randint(1,1000) for _ in range(N)]
print(podciag(t))