from random import randint


def prog(tab):
    maxe = mine = 0
    cmax = cmin = 0
    for i in range(len(tab)):
        if tab[i] == maxe:
            cmax += 1
        elif tab[i] > maxe:
            cmax = 1
            maxe = tab[i]
        elif tab[i] == mine:
            cmin += 1
        elif tab[i] < mine:
            cmin = 1
            mine = tab[i]
    if cmax == cmin == 1:
        return True
    return False


N = int(input("> "))
t = [randint(-1000, 1000) for _ in range(N)]
print(prog(t))
