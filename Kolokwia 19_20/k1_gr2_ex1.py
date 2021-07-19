from math import sqrt, ceil


def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 or num%3 == 0:
        return False

    i = 5
    while i <= sqrt(num):
        if num%i == 0:
            return False
        i += 2
        if num%i == 0:
            return False
        i += 4
    #end while
    return True
#end def


def iloczyn_pierwszych(num):
    pierwsze = [0]*(num//2)
    ind = 0
    for p in range(2, ceil(sqrt(num) + 1)):
        pierwsze[ind] = p
        ind += 1

    for p in range(len(pierwsze)):
        for r in range(len(pierwsze)):
            if p*r > num:
                break
            if p*r == num:
                return True
        if p > num//2:
            break
    #end for
    return False
#end def


def kawalki(t1, t2):
    n = len(t1)
    for dl_k in range(n):
        end = n-dl_k+1
        for start1 in range(end):
            suma1 = 0
            for el1 in range(start1, start1+dl_k):
                suma1 += t1[el1]

            for start2 in range(end):
                suma2 = 0
                for el2 in range(start2, start2+dl_k):
                    suma2 += t2[el2]

                suma = suma1 + suma2
                if iloczyn_pierwszych(suma):
                    return True
            #end for
        #end for
    #end for
    return False
#end def