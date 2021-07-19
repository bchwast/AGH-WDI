def count5(N):
    podzielne = False
    count = 0
    while N >= 4:
        if N%5 == 0:
            podzielne = True
            copy = N
            while copy%5 == 0:
                copy //= 5
                count += 1
            #end while
        #end if
        if podzielne:
            N -= 5
        else:
            N -= 1
    #end while
    return count
#end def


def last_non0_dig(N):
    num_of2 = num_of5 = count5(N)
    res = 1
    while N > 0:
        copy = N
        while copy%5 == 0 and num_of5 > 0:
            copy //= 5
            num_of5 -= 1
        #end while
        while copy%2 == 0 and num_of2 > 0:
            copy //= 2
            num_of2 -= 1
        #end while
        res *= copy
        if res > 10:
            res = res%10
        #end if
        N -= 1
    #end while
    return res
#end def


print(last_non0_dig(3000))
