from random import randint

def rewers(tab):
    MAX = len(tab)
    dl_m = 0
    for i in range(MAX):
        p = i
        k = MAX - 1
        while k > p:
            dl = 0
            if tab[p] == tab[k]:
                dl += 1
                c_p = p + 1
                c_k = k - 1
                while c_k > c_p and tab[c_p] == tab[c_k]:
                    dl += 1
                    c_p += 1
                    c_k -= 1
                #end while
                if dl > dl_m:
                    dl_m = dl
            #end if
            k -= 1
        #end while
    #end for
    return dl_m
#end def


tab = [randint(100,999) for _ in range(100)]
print(rewers(tab))