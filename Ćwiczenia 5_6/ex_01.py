def spirala(tab):
    n = 1
    k = N
    for i in range(N//2 + 1):
        for j in range(i,k):
            tab[i][j] = n
            n += 1
        for j in range(k-1-i):
            tab[i+j+1][k-1] = n
            n += 1
        for j in range(k-2,i-1,-1):
            tab[k-1][j] = n
            n += 1
        for j in range(k-2,i,-1):
            tab[j][i] = n
            n += 1
        k -= 1
    return tab


N = int(input("> "))
T = []
for i in range(N):
    T.append([])
    for j in range(N):
        T[i].append(0)
T = spirala(T)
for i in range(N):
    print("[",end="")
    for j in range(N-1):
        print(T[i][j],end=",")
    print(T[i][N-1],"]",sep="")
