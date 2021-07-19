def skoczek(tab, iloczyn):
    N = len(tab)
    counter = 0
    for i in range(N):
        for j in range(N):
            if i >= 1:
                if j >= 2:
                    if tab[i][j]*tab[i-1][j-2] == iloczyn:
                        counter += 1
                if j <= (N-1)-2:
                    if tab[i][j]*tab[i-1][j+2] == iloczyn:
                        counter += 1
            if i >= 2:
                if j >= 1:
                    if tab[i][j]*tab[i-2][j-1] == iloczyn:
                        counter += 1
                if j <= (N-1)-1:
                    if tab[i][j]*tab[i-2][j+1] == iloczyn:
                        counter += 1
            if i <= (N-1)-2:
                if j >= 1:
                    if tab[i][j]*tab[i+2][j-1] == iloczyn:
                        counter += 1
                if j <= (N-1)-1:
                    if tab[i][j]*tab[i+2][j+1] == iloczyn:
                        counter += 1
            if i <= (N-1)-1:
                if j >= 2:
                    if tab[i][j]*tab[i+1][j-2] == iloczyn:
                        counter += 1
                if j <= (N-1)-2:
                    if tab[i][j]*tab[i+1][j+2] == iloczyn:
                        counter += 1
    counter //= 2
    return counter
