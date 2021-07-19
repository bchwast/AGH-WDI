from random import randint


def podciag(tab):
    len_m = 1
    len_new = 1
    tempv = tab[0]
    tempi = 0
    for i in range(N-1):
        if tab[i+1] - tab[i] > 0:
            tempv += tab[i+1]
            tempi += i + 1
            if tempi == tempv:
                len_new += 1
            else:
                tempv = tab[i+1]
                tempi = i + 1
                len_new = 1
        else:
            tempv = tab[i+1]
            tempi = i + 1
            len_new = 1
        if len_new > len_m:
            len_m = len_new
    if len_m > 1:
        return len_m
    return 0


N = int(input("> "))
t = [randint(1,10000) for _ in range(N)]
print(podciag(t))