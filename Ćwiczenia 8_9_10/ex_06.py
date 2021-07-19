def sumy(tab, ind=0, s_el=0, s_ind=0):
    if s_el == s_ind and (s_el != 0 or tab[0] == 0):
        return s_el
    for i in range(ind + 1, len(tab)):
        return sumy(tab, i, s_el+tab[i], s_ind+i) or sumy(tab, i, s_el, s_ind)
#end def


print(sumy([1,7,3,5,11,2]))