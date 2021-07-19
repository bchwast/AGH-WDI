def waga(t, m, o=0):
    if m == 0:
        return True
    if o == len(t):
        return False
    return waga(t, m-t[o], o+1) or waga(t, m, o+1)
#end def

print(waga([5,4,2],10))
