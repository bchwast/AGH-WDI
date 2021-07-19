def can_he(szach, w, k):
    if k > 0:
        for i in range(k):
            dw = abs(w - szach[i])
            dk = abs(k - i)
            if dw == dk or szach[i] == w:
                return False
    return True
#end def


def hetmany(szach, w=0, k=0):
    if k == 8:
        print(szach)
        exit(0)
    for i in range(8):
        szach[k] = i
        if can_he(szach, i, k):
            hetmany(szach, i, k+1)
    #end for
    szach[k] = None
#end def


szach = [None]*8
hetmany(szach)
print(szach)