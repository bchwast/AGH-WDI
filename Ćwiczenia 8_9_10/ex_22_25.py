def czynnik(num):
    lista = []
    num_c = num
    kolejna = True
    i = 2
    while i < num:
        if num_c%i == 0:
            if kolejna:
                lista.append(i)
            num_c //= i
            kolejna = False
        else:
            i += 1
            kolejna = True
    #end while
    return lista
#end def


def skoki(T, ind=0, ruchy=0):
    if ind >= len(T):
        return False
    if ind == len(T) - 1:
        return ruchy

    for el in czynnik(T[ind]):
        ret = skoki(T, ind+el, ruchy+1)
        if ret:
            return ret
    return False
#end def


def garek(T):
    ret = skoki(T)
    if not ret:
        return -1
    return ret
#end def

