from math import sqrt


def distance(subset, n):
    x = y = 0
    for i in range(n+1):
        x += subset[i][0]
        y += subset[i][1]
    return sqrt((x/(n+1))**2 + (y/(n+1))**2)
#end def


def check(subset, n, k, r):
    if n+1 >= k or (n+1)%3 != 0 or distance(subset, n) >= r:
        return False
    return True
#end def


def mass(T, subset, k, r, n=-1, ind=0):
    if n + 1 >= 1:
        if check(subset, n, k, r):
            return True
    #end if
    if ind < len(T):
        if mass(T, subset, k, r, n, ind+1):
            return True
        subset[n+1] = T[ind]
        if mass(T, subset, k, r, n+1, ind+1):
            return True
    return False
#end def


def pary(T, r, k):
    return mass(T, [None]*len(T), k, r)
#end def


T = [(1,1), (2,2), (3,3)]
print(pary(T, 3, 4))