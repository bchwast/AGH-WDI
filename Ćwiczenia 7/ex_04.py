from ex_01 import roznica, iloraz, skracanie


def ciagi(tab):
    n = len(tab)
    la = lg = 0
    i = 0
    while i < n-1:
        r = skracanie(roznica(tab[i+1],tab[i]))
        dl = 1
        while i < n-1 and skracanie(roznica(tab[i+1],tab[i])) == r:
            i += 1
            dl += 1
        #end while
        if dl > 2:
            la += 1
        #end if
    #end while

    i = 0
    while i < n-1:
        if tab[i] == (0,1):
            dl = 1
            while i < n-1 and tab[i+1] == tab[i]:
                dl += 1
                i += 1
            #end while
            if dl > 2:
                lg += 1
            i += 1
        #end if

        q = skracanie(iloraz(tab[i+1],tab[i]))
        dl = 1
        while i < n-1 and skracanie(iloraz(tab[i+1],tab[i])) == q:
            i += 1
            dl += 1
        #end while
        if dl > 2:
            lg += 1
        #end if
    #end while

    if la > lg:
        return 1
    if la < lg:
        return -1
    return 0
#end def


tab = [(1,1),(2,1),(3,1),(4,1),(0,1),(0,1),(0,1),(0,1),(5,1),(25,1),(125,1),(127,1),(129,1)]
print(ciagi(tab))