from math import sqrt


def prime(liczba):
    if liczba == 2 or liczba == 3:
        return True
    elif liczba < 2 or liczba%2 == 0 or liczba%3 == 0:
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


def cyferki(tab):
    N = len(tab)
    count = 0
    for i in range(N):
        for j in range(N):
            komorka = tab[i][j]
            jest = True
            while komorka > 0:
                if not prime(komorka%10):
                    jest = False
                    break
                else:
                    komorka //= 10
            if jest:
                count += 1
                break
    if count == N-1:
        return True
    return False
