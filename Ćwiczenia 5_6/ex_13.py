from math import sqrt


def prime(liczba):
    if liczba == 2 or liczba == 3:
        return True
    elif liczba <= 1 or liczba%2 == 0 or liczba%3 == 0:
        return False
    licznik = 5
    while licznik <= sqrt(liczba):
        if liczba%licznik == 0:
            return False
        licznik += 2
        if liczba%licznik == 0:
            return False
        licznik += 4
    return True


def komplementarne(tab):
    N = len(tab)
    for i in range(N):
        for j in range(N):
            l1 = tab[i][j]
            zerowac = True
            for a in range(N):
                for b in range(N):
                    if a != i and b != j:
                        if prime(tab[a][b] + l1):
                            zerowac = False
            if zerowac:
                tab[i][j] = 0
    