def waga(t, m, o=0, odw=[]):
    odw.append(t[o])
    if m < 0:
        odw.pop()
        return False
    if m == 0:
        return True
    if o == len(t):
        odw.pop()
        return False
    return waga(t, m-t[o], o+1, odw) or waga(t, m, o+1, odw) or waga(t, m+t[o], o+1, odw)
#end def

waga([1,3,5,10,16,24],24)