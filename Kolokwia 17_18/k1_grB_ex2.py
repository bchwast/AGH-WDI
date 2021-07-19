def palindrom(tab):
    N = 1000
    l_max = 0
    for i in range(N):
        beg = i
        for end in range(N-1,i,-1):
            l_curr = end - beg + 1
            while beg < end:
                if tab[beg] != tab[end] or tab[beg]%2 == 0:
                    break
                beg += 1
                end -= 1
            else:
                if l_curr > l_max:
                    l_max = l_curr
        #end for
    #end for
    return l_max
