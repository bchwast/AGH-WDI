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
    pdcg = [2 for i in range(N)]
    a = 0
    q = 0
    for i in range(len(tab)-1):
        if tab[i+1] / tab[i] == q:
            pdcg[a] += 1
        else:
            a += 1
            q = tab[i+1] / tab[i]
    pdcg = sortuj(pdcg)
    return pdcg[0]

N = int(input("> "))
t = [randint(1,10) for _ in range(N)]
print(podciag(t))