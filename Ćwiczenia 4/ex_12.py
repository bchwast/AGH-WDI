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

def podciag(tab, jaki):
    pdcg = [1 for i in range(N)]
    if jaki == "ros":
        r = 1
    else:
        r = -1
    a = 0
    for i in range(len(tab)-1):
        if jaki == "ros":
            if tab[i+1] - tab[i] == r:
                pdcg[a] += 1
            elif tab[i+1] - tab[i] > 0:
                a += 1
                r = tab[i+1] - tab[i]
        else:
            if tab[i+1] - tab[i] == r:
                pdcg[a] += 1
            elif tab[i+1] - tab[i] < 0:
                a += 1
                r = tab[i+1] - tab[i]
    pdcg = sortuj(pdcg)
    return pdcg[0]


N = int(input("> "))
t = [(2*randint(0,9))+1 for _ in range(N)]
print(podciag(t, "ros") - podciag(t, "mal"))