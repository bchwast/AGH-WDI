def area(squer):
    return (squer[1]-squer[0])**2
#end def


def kwadraty(T, n, suma, wybrane, ind=0):
    for i in range(ind, len(T) - n + 1):
        for j in range(14 - n):
            if wybrane[j][0] <= T[i][0] <= wybrane[j][1] or wybrane[j][0] <= T[i][1] <= wybrane[j][1]:
                return False
            elif wybrane[j][2] <= T[i][2] <= wybrane[j][3] or wybrane[j][2] <= T[i][3] <= wybrane[j][3]:
                return False
        suma += area(T[i])
        if n == 1:
            if suma == 2012:
                return True
        wybrane[13-n] = T[i]
        res = kwadraty(T, n-1, suma, wybrane, i+1)
        if res:
            return True
    return False
#end def


kwadraty(T, 13, 0, [0 for _ in range(13)])

