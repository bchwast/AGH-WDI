def is_not_even(num):
    jed = 0
    while num > 0:
        if num%2 == 1:
            jed += 1
        num //= 2
    if jed%2 == 0:
        return True
    return False


def usuwanie(tab):
    n = len(tab)
    for rem_w in range(n):
        for rem_k1 in range(n):
            for rem_k2 in range(n):
                if rem_k1 != rem_k2:
                    okay = True
                    for w in range(n):
                        if okay:
                            for k in range(n):
                                if w != rem_w and k != rem_k1 and k != rem_k2:
                                    if not is_not_even(tab[w][k]):
                                        okay = False
                                        break
                            #end for
                        else:
                            break
                    #end for
                    if okay:
                        return True
            #end for
        #end for
    #end for
    return False
#end def