def szach(t):
    n = len(t)
    sz = [None]*n
    wiersz = [False]*n
    przek1 = [False]*(2*n-1)
    przek2 = [False]*(2*n-1)

    def suma(t, sz):
        s = 0
        for i in range(n):
            s += t[sz[i]][i]
        print(s)
        return s == 0
    #end def


    def hetman(w=0, k=0):
        if wiersz[w] or przek1[w + k] or przek2[n - 1 + w - k]:
            return False

        sz[k] = w
        if k != n-1:
            wiersz[w] = przek1[w + k] = przek2[n - 1 + w - k] = True
            for i in range(n):
                if hetman(i, k+1):
                    return True
            wiersz[w] = przek1[w + k] = przek2[n - 1 + w - k] = False
        else:
            if suma:
                return True
            return False
    #end def


    return hetman()
#end def

T = [[1 for _ in range(8)] for _ in range(8)]
print(szach(T))

