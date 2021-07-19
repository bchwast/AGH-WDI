def suma(zb, end):
    suma = 0
    for i in range(end+1):
        suma += zb[i]
    return suma


def core(t, zb1, zb2, ind1=-1, ind2=-1, ind=-1):
    if ind1 == ind2 and ind1 > -1:
        if suma(zb1, ind1) == suma(zb2, ind2):
            return True

    if ind == len(t) - 1:
        return False

    if core(t, zb1, zb2, ind1, ind2, ind+1):
        return True

    zb1[ind1+1] = t[ind+1]
    if core(t, zb1, zb2, ind1+1, ind2, ind+1):
        return True

    zb2[ind2+1] = t[ind+1]
    if core(t, zb1, zb2, ind1, ind2+1, ind+1):
        return True

    return False
#end def


def podzbiory(t):
    zb1 = [None]*len(t)
    zb2 = [None]*len(t)
    return core(t, zb1, zb2)
#end def


t = [1, 3, 2, 2]
print(podzbiory(t))