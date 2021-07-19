def kwadrat(t, k):
    N = 1000
    for bok in range(2, 1000, 2):
        for r in range(1000-bok):
            for c in range(1000-bok):
                if t[r][c]*t[r][c+bok]*t[r+bok][c+bok]*t[r+bok][c] == k:
                    return (r+(bok//2), c+(bok//2))
            #end for
        #end for
    #end for
    return False
#end def
