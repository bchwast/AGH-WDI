def wielokrotnosc(num):
    i = 2
    while num >= 2*i*i:
        dod = i*i
        j = 2*dod
        while num >= j:
            if num == j:
                return True
            j += dod
        i += 1
    #end while
    return False
#end def


def wycinianie(tab):
    n = len(tab)
    for rem_w in range(n):
        for rem_k1 in range(n):
            for rem_k2 in range(n):
                if rem_k1 != rem_k2:
                    okay = True
                    for w in range(n):
                        for k in range(n):
                            if w != rem_w and k != rem_k1 and k != rem_k2:
                                if not wielokrotnosc(tab[w][k]):
                                    okay = False
                                    break
                        #end for
                        if not okay:
                            break
                    #end for
                    if okay:
                        return True
            #end for
        #end for
    #end for
    return False
#end def
