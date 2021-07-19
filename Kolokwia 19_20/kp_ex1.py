def nwd(a, b):
    while b != 0:
        b, a = a%b, b
    #end while
    return a
#end def


def mag_mino(tab):
    n = len(tab)
    for m1w in range(n):
        for m1k1 in range(n-1):
            for m2w1 in range(n-1):
                if m2w1 != m1w and m2w1+1 != m1w:
                    for m2k in range(n):
                        if m2k != m1k1 and m2k != m1k1+1:
                            k_1 = tab[m1w][m1k1]
                            k_2 = tab[m1w][m1k1+1]
                            k_3 = tab[m2w1][m2k]
                            k_4 = tab[m2w1+1][m2k]
                            if nwd(k_1, k_2) == nwd(k_1, k_3) == nwd(k_1, k_4) == nwd(k_2, k_3) == nwd(k_2, k_4) == nwd(k_3, k_4) == 1:
                                return True
                    #end for
            #end for
        #end for
    #end for
    return False
#end def
