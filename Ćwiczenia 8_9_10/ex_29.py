from math import sqrt


def distance(subset, n):
    x = y = z = 0
    for i in range(n+1):
        x += subset[i][0]
        y += subset[i][1]
        z += subset[i][2]
    x /= (n+1)
    y /= (n+1)
    z /= (n+1)
    return sqrt(x**2 + y**2 + z**2)
#end def


def mass(T, subset, r, ind=0, n=-1):
    if n >= 2:
        if distance(subset, n) <= r:
            return True
    #end if
    if ind < len(T):
        if mass(T, subset, r, ind+1, n):
            return True
        subset[n+1] = T[ind]
        if mass(T, subset, r, ind+1, n+1):
            return True
    return False
#end def


def trojki(T, r):
    return mass(T, [None]*len(T), r)
#end def


T = [(1,1,1), (2,2,2), (3,3,3)]
print(trojki(T, sqrt(3)))