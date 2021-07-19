# Bartłomiej Chwast
# funkcja sprawdza w kazdym napisie czy i jesli tak to ile razy powtarza się dany podnapis

def multi(T):
    n = len(T)
    dl_m = 0
    for i in range(n):
        dl = len(T[i])
        for j in range(dl):
            length = 0
            for k in range(dl):
                if T[i][j] == T[i][k]:
                    length += 1
                #end for
            if dl_m < length:
                dl_m = length
            #end if
        #end for
    #end for
    return dl_m
#end def
