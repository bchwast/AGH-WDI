from random import randint


def kwadrat(tab, k):
    wiersz = kolumna = 0
    for i in range(N):
        for j in range(N):
            for a in range(2,N,2):
                if i+a < N and j+a < N:
                    if tab[i][j]*tab[i+a][j]*tab[i+a][j+a]*tab[i][j+a] == k:
                        kolumna = j + a//2
                        wiersz = i + a//2
                        return True, wiersz, kolumna
    return False



N = int(input("> "))
k = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for _ in range(N):
        T[i].append(randint(1,100))

print(T)
print(kwadrat(T,k))
