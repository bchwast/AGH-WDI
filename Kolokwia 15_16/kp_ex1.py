def fibo(l1, l2):
    if l1 == l2 == 1:
        return True

    a = 1
    b = 1
    while a <= l2:
        if a == l2 and b == l1:
            return True
        a, b = a+b, a
    #end while
    return False
#end def


def ciag(t):
    N = len(t)
    for i in range(N):
        for j in range(N-2):
            if fibo(t[i][j], t[i][j+1]) and t[i][j+2] == (t[i][j+1]+t[i][j]):
                    return i
        #end for
    #end for
    return -1
#end def


