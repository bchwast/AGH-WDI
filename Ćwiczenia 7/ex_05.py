def kwadrat(dane):
    x = 0
    y = 1
    n = len(dane)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if a != b != c != d:
                        if dane[a][y] == dane[b][y] and dane[c][y] == dane[d][y]\
                            and dane[a][x] == dane[d][x] and dane[b][x] == dane[c][x]:
                            x1 = min(dane[a][x], dane[b][x])
                            x2 = max(dane[a][x], dane[b][x])
                            y1 = min(dane[a][y], dane[d][y])
                            y2 = max(dane[a][y], dane[d][y])
                            punkty = False
                            for p in range(n):
                                if dane[p][x] > x1 and dane[p][x] < x2 and dane[p][y] > y1 and dane[p][y] < y2:
                                    punkty = True
                            #end for
                            if not punkty:
                                return True
                        #end if
                    #end if
                #end for
            #end for
        #end for
    #end for
    return False
#end def


dane = [(1,1),(8,3),(8,8),(12,3),(4,4),(1,2),(4,8),(6,15),(8,4)]
print(kwadrat(dane))