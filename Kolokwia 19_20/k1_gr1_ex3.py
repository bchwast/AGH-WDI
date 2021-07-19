def ruchy(sz, w, k, mode):
    pos_w = [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    pos_k = [-2, -1, 0, 1, 2, 2, 1, 0, -1, -2, -2, -1, 0 ,1 ,2, 2, 1, 0, -1, -2]
    w = w+pos_w[mode]
    k = k+pos_k[mode]
    if w < 0 or k < 0 or w >= len(sz) or k >= len(sz):
        return True
    if sz[w][k]:
        return False
    return True
#end def


def ustawianie(t, sz, w=-1, k=0, suma=0):
    if w > -1:
        suma += t[w][k]
        sz[w][k] = True

    if w == len(t)-1:
        if suma == 0:
            return True
        sz[w][k] = False

    if w < len(t)-1:
        for i in range(len(t)):
            dalej = False
            for ruch in range(20):
                if not ruchy(sz, w+1, i, ruch):
                    dalej = True
                    break
            if not dalej:
                if ustawianie(t, sz, w+1, i, suma):
                    return True
        #end for
        if w > -1:
            sz[w][k] = False
#end def


def krole(t):
    sz = [[False for _ in range(len(t))] for _ in range(len(t))]
    if ustawianie(t, sz):
        return True
    return False
#end def


T = [[0 for _ in range(8)] for _ in range(8)]
print(krole(T))

