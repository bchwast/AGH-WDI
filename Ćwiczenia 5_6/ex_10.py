from random import randint


def szukajzer(tab):
    for i in range(N):
        jest_zero = False
        for j in range(N):
            komorka = tab[i][j]
            if komorka == 0:
                jest_zero = True
        if not jest_zero:
            return False
    for i in range(N):
        jest_zero = False
        for j in range(N):
            komorka = tab[j][i]
            if komorka == 0:
                jest_zero = True
        if not jest_zero:
            return False
    return True


N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for _ in range(N):
        T[i].append(randint(-100,100))
print(T)
print(szukajzer(T))