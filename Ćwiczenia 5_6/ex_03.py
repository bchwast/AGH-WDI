from random import randint


def parz(tab):
    for i in range(N):
        licznik = 0
        for j in range(N):
            liczba = tab[i][j]
            parz = False
            while liczba > 0 and not parz:
                if (liczba%10)%2 == 0:
                    licznik += 1
                    parz = True
                else:
                    liczba //= 10
        if licznik == N:
            return True
    return False


N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for _ in range(N):
        T[i].append(0)

for i in range(N):
    for j in range(N):
        T[i][j] = randint(1,99)

print(parz(T))