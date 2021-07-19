def podciag(tab):
    n = len(tab)
    dl_m = -1
    for start in range(n):
        suma_ind = start
        suma_el = tab[start]
        ind = start
        dl = 1
        while ind < n-1 and tab[ind] < tab[ind+1]:
            suma_ind += ind+1
            suma_el += tab[ind+1]
            dl += 1
            if suma_el == suma_ind:
                dl_m = max(dl_m, dl)
            ind += 1
    #end for
    if dl_m <= 1:
        return 0
    return dl_m
#end def

