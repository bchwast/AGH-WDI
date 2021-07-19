def otoczenie(tab):
    N = len(tab)
    suma_max = 0
    wiersz = kolumna = -1
    for i in range(N):
        for j in range(N):
            suma = 0
            if i != 0:
                suma += tab[i-1][j]
            if i != N-1:
                suma += tab[i+1][j]
            if j != 0:
                suma += tab[i][j-1]
            if j != N-1:
                suma += tab[i][j+1]
            if i != 0 and j != 0:
                suma += tab[i-1][j-1]
            if i != 0 and j != N-1:
                suma += tab[i-1][j+1]
            if i != N-1 and j != 0:
                suma += tab[i+1][j-1]
            if i != N-1 and j != N-1:
                suma += tab[i+1][j+1]
            if suma > suma_max:
                suma_max = suma
                kolumna = j
                wiersz = i
    return wiersz, kolumna