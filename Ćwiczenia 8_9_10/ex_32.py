def suma(subset, n):
    s = 0
    for i in range(n+1):
        s += subset[i]
    return s
#end def


def core(T, subset1, subset2, k, n1=-1, n2=-1, ind=0):
    if n1+1 == n2+1 == k:
        if suma(subset1, n1) == suma(subset2, n2):
            return True
    #end if
    if ind < len(T):
        if core(T, subset1, subset2, k, n1, n2, ind+1):
            return True
        subset1[n1+1] = T[ind]
        if core(T, subset1, subset2, k, n1+1, n2, ind+1):
            return True
        subset2[n2+1] = T[ind]
        if core(T, subset1, subset2, k, n1, n2+1, ind+1):
            return True
    return False
#end def


def subsets(T, k):
    return core(T, [None]*len(T), [None]*len(T), k)
#end def


T = [1,1,2,1,5,4,12]
print(subsets(T, 2))