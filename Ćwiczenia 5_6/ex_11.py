def friends(tab):
    def friend(liczba, wzor):
        while liczba > 0:
            if liczba%10 not in wzor:
                return False
            liczba //= 10
        return True


    z_cyfr = [10]*10
    N = len(tab)
    only_f = 0
    for i in range(N):
        for j in range(N):
            liczba = tab[i][j]
            a = 0
            while liczba > 0:
                for k in range(10):
                    if liczba%10 != z_cyfr[k]:
                        z_cyfr[a] = liczba%10
                        a += 1
                liczba //= 10
            if i == 0:
                if j == 0:
                    if friend(tab[i][j+1],z_cyfr) and friend(tab[i+1][j],z_cyfr):
                        only_f += 1
                elif j == N-1:
                    if friend(tab[i][j-1],z_cyfr) and friend(tab[i+1][j],z_cyfr):
                    only_f += 1
                else:
                    if friend(tab[i][j-1],z_cyfr) and friend(tab[i][j+1],z_cyfr) and friend(tab[i+1][j],z_cyfr):
                        only_f += 1
            elif i == N-1:
                if j == 0:
                    if friend(tab[i][j+1],z_cyfr) and friend(tab[i-1][j],z_cyfr):
                        only_f += 1
                elif j == N-1:
                    if friend(tab[i][j-1],z_cyfr) and friend(tab[i-1][j],z_cyfr):
                        only_f += 1
                else:
                    if friend(tab[i][j+1],z_cyfr) and friend(tab[i-1][j],z_cyfr) and friend(tab[i][j-1],z_cyfr):
                        only_f += 1
            else:
                if j == 0:
                    if friend(tab[i][j+1],z_cyfr) and friend(tab[i-1][j],z_cyfr) and friend(tab[i+1][j],z_cyfr):
                        only_f += 1
                elif j == N-1:
                    if friend(tab[i][j-1],z_cyfr) and friend(tab[i-1][j],z_cyfr) and friend(tab[i+1][j],z_cyfr):
                        only_f += 1
                else:
                    if friend(tab[i][j+1],z_cyfr) and friend(tab[i-1][j],z_cyfr) and friend(tab[i+1][j],z_cyfr) and friend(tab[i][j-1],z_cyfr):
                        only_f += 1
    return only_f




