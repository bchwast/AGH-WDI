def hetmany(dane):
    N = len(dane)
    for het1 in range(N-1):
        for het2 in range(het1+1,N):
            if dane[het1][0] == dane[het2][0]:
                return False
            if dane[het1][1] == dane[het2][1]:
                return False
            if abs(dane[het1][0] - dane[het2][0]) == abs(dane[het1][1] - dane[het2][1]):
                return False
        #end for
    #end for
    return True
#end def


dane = [(1,60),(3,61),(2,21),(4,45),(9,41)]
print(hetmany(dane))
