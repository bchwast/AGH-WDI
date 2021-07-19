from random import randint


def iloraz(tab):
    wiersz = kolumna = 0
    maxil = 0
    for i in range(N):
        sumaw = 0
        for a in range(N):
            sumaw += tab[i][a]
        for j in range(N):
            sumak = 0
            for a in range(N):
                sumak += tab[a][j]
            if sumak/sumaw > maxil:
                wiersz = i
                kolumna = j
                maxil = sumak/sumaw
    return wiersz,kolumna



N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for _ in range(N):
        T[i].append(0)

for i in range(N):
    for j in range(N):
        T[i][j] = randint(1,99)
print(T)
print(iloraz(T))