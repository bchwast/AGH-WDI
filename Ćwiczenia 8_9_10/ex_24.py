from math import sqrt, inf


def srodek(subset, n):
    x = y = 0
    for i in range(n+1):
        x += subset[i][0]
        y += subset[i][1]
    return (x/(n+1), y/(n+1))
#end def


def distance(subset1, subset2, n1, n2):
    s1 = srodek(subset1, n1)
    s2 = srodek(subset2, n2)
    return sqrt((s1[0] - s2[0])**2 + (s1[1] - s2[1])**2)
#end def


def subsets(T, subset1, subset2, dist, ind=0, n1=-1, n2=-1):
    if n1 >= 0 and n2 >= 0:
        dist[0] = min(dist[0], distance(subset1, subset2, n1, n2))
    #end if
    if ind < len(T):
        subsets(T, subset1, subset2, dist, ind+1, n1, n2)
        subset1[n1+1] = T[ind]
        subsets(T, subset1, subset2, dist, ind+1, n1+1, n2)
        subset2[n2+1] = T[ind]
        subsets(T, subset1, subset2, dist, ind+1, n1, n2+1)
    return dist[0]
#end def


def minimum(T):
    return subsets(T, [None]*len(T), [None]*len(T), [inf])
#end def



T = [(1,1), (6,2), (3,3), (8,5)]
print(minimum(T))