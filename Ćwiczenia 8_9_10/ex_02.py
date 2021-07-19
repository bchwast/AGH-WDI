def waga(n):
    i = 2
    kolejna = True
    w = 0
    while n > 1:
        if n%i == 0:
            if kolejna:
                w += 1
            n //= i
            kolejna = False
        else:
            i += 1
            kolejna = True
    #end while
    return w
#end def


def rownewagi(T):
    def dzielenie(t, i=0, s_1=0, s_2=0, s_3=0):
        if i == len(t):
            if s_1 == s_2 == s_3:
                return True
        else:
            val = t[i]
            return dzielenie(t, i+1, s_1 + val, s_2, s_3) or\
                    dzielenie(t, i+1, s_1, s_2 + val, s_3) or\
                    dzielenie(t, i+1, s_1, s_2, s_3 + val)
        return False
    #end def

    N = len(T)
    t_wag = [waga(T[i]) for i in range(N)]
    if dzielenie(t_wag, N):
        return True
    return False
#end def


T = [2, 2, 8, 2, 6]
print(rownewagi(T))