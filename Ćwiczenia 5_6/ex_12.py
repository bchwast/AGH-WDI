def zlozona(liczba):
    if liczba <= 3 or liczba == 5:
        return False
    if liczba%2 == 0 or liczba%3 == 0:
        return True
    a = 6
    while a < liczba//2:
        if liczba%(a-1) == 0 or liczba%(a+1) == 0:
            return True
        a += 6
    return False


def trzywymiary(T):
    N = len(T)
    elementy = [0]*N
    for z in range(N):
        for y in range(N):
            for x in range(N):
                dobry_s = 0
                if x != N-1:    #w prawo
                    if zlozona(T[z][y][x+1]):
                        dobry_s += 1
                if x != N-1 and y != N-1:   #w prawo dół
                    if zlozona(T[z][y+1][x+1]):
                        dobry_s += 1
                if y != N-1:    #w dół
                    if zlozona(T[z][y+1][x]):
                        dobry_s += 1
                if x != 0 and y != N-1: #w lewo dół
                    if zlozona(T[z][y+1][x-1]):
                        dobry_s += 1
                if x != 0:  #w lewo
                    if zlozona(T[z][y][x-1]):
                        dobry_s += 1
                if x != 0 and y != 0:   #w lewo góra
                    if zlozona(T[z][y-1][x-1]):
                        dobry_s += 1
                if y != 0:  #góra
                    if zlozona(T[z][y-1][x]):
                        dobry_s += 1
                if x != N-1 and y != 0: #w prawo góra
                    if zlozona(T[z][y-1][x+1]):
                        dobry_s += 1
                if dobry_s >= 6:
                    elementy[z] += 1
            #end for
        #end for
        if z > 0:
            if elementy[z] != elementy[z-1]:
                return False
    #end for
    return True
