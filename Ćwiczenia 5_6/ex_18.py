def podciag(tab):
    N = len(tab)
    suma_m = suma_t = 0
    for i in range(N):
        for j in range(N):
            l = N
            if i + 10 < N:
                l = i + 10
            for a in range(i,l):
                suma_t += tab[a][j]
            if suma_t > suma_m:
                suma_m = suma_t
            suma_t = 0
            if j + 10 < N:
                l = j + 10
            else:
                l = N
            for a in range(j,l):
                suma_t += tab[i][a]
            if suma_t > suma_m:
                suma_m = suma_t
            suma_t = 0
    return suma_m
