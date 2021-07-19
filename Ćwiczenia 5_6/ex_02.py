from random import randint


def niep(tab):
    parz = False
    nieparz = False
    for i in range(N):
        for j in range(N):
            liczba = tab[i][j]
            parz = False
            while liczba > 0 and not parz:
                if (liczba%10)%2 == 1:
                    liczba //= 10
                else:
                    parz = True
            if not parz:
                nieparz = True
                break
        if not nieparz:
            return False
        parz = nieparz = False
    return True


N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for j in range(N):
        T[i].append(0)

for i in range(N):
    for j in range(N):
        T[i][j] = randint(1,99)

print(T)
print(niep(T))