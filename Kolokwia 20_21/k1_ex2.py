def compare(T, a, b):
    i = 0
    while T[a][i] == T[b][i]:
        i += 1
    #end while
    return T[a][i] > T[b][i]
#end def


def distance(T):
    N = len(T)
    i_max = i_min = 0
    for i in range(N):
        if compare(T, i, i_max):
            i_max = i
        #end if
        if compare(T, i_min, i):
            i_min = i
        #end if
    #end for
    return abs(i_max - i_min)
#end def
