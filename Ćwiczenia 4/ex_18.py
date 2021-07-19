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


def prog(tab):
    pdcg = [0 for _ in range(N)]
    a = 0
    for i in range(len(tab)):
        for j in range(len(tab)-1,i+1,-1):
            ci = i
            cj = j
            while tab[ci]%2 == tab[cj]%2 == 1 and tab[cj] == tab[ci] and ci < cj:
                pdcg[a] += 2
                ci += 1
                cj -= 1
            if ci == cj and tab[ci] == tab[cj] and tab[ci]%2 == tab[cj]%2 == 1:
                pdcg[a] += 1
                a += 1
            elif ci <= cj:
                pdcg[a] = 0
            else:
                a += 1
    pdcg = sortuj(pdcg)
    if pdcg[0] > 1:
        return pdcg[0]
    return 0


N = int(input("> "))
t = [randint(1, 1000) for _ in range(N)]
print(prog(t))
