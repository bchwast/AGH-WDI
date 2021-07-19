from random import randint


def ciag(tab):
    dlmax = 2
    for i in range(N-2):
        for j in range(N-2):
            if dlmax >= (N-2)-j and dlmax >= (N-2)-i:
                continue
            q = tab[i+1][j+1]/tab[i][j]
            checkq = q
            a = 1
            dl = 2
            while checkq == q and i+a+1 < N and j+a+1 < N:
                checkq = tab[i+a+1][j+a+1]/tab[i+a][j+a]
                a += 1
                dl += 1
            if dl > dlmax:
                dlmax = dl
    if dlmax >= 3:
        return True, dlmax
    return False


N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for _ in range(N):
        T[i].append(randint(1,10))
print(T)
print(ciag(T))