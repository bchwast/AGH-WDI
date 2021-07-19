# "True" w tablicy "t" to obecnosc wiezy, "False" to jej brak

def szachuje(t):
    wiersze = [False]*201
    kolumny = [False]*201
    for i in range(201):
        for j in range(201):
            if t[i][j]:
                wiersze[i] = True
                kolumny[j] = True
        #end for
    #end for
    for i in range(201):
        if not wiersze[i] or not kolumny[i]:
            return False
    #end for
    return True
#end def

def wieze(t):
    for w1 in range(201):
        for k1 in range(201):
            if t[w1][k1]:
                for w2 in range(201):
                    for k2 in range(201):
                        if w1 != w2 and k1 != k2 and not t[w2][k2]:
                            t[w1][k1] = False
                            t[w2][k2] = True
                            if szachuje(t):
                                return (w1, k1), (w2, k2)
                            t[w1][k1] = True
                            t[w2][k2] = False
                    #end for
                #end for
        #end for
    #end for
    return False
#end def