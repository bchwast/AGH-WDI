def wieze(t):
    N = len(t)
    s_m = 0
    wie1 = wie2 = None
    for w1 in range(N):
        for k1 in range(N):
            s1 = 0
            for i in range(N):
                if i != k1:
                    s1 += t[w1][i]
            #end for
            for i in range(N):
                if i != w1:
                    s1 += t[i][k1]
            #end for
            for w2 in range(N):
                for k2 in range(N):
                    s2 = 0
                    if w2 != w1:
                        for i in range(N):
                            if i != k2:
                                s2 += t[w2][i]
                        #end for
                    #end if
                    if k2 != k1:
                        for i in range(N):
                            if i != w2:
                                s2 += t[i][k2]
                        #end for
                    #end if
                    if s1 + s2 > s_m:
                        s_m = s1 + s2
                        wie1 = (w1, k1)
                        wie2 = (w2, k2)
                    #end if
                #end for
            #end for
        #end for
    #end for
    return wie1, wie2
#end def


t = [[0, 20, 0, 0, 0, 0],[20, 20, 20, 20, 20, 20],[0, 20, 0 ,0 ,0 ,0],[0, 20, 0, 0, 0, 0],[0, 20, 0, 0, 0, 0],[0, 20, 0, 0, 0 ,0]]
print(wieze(t))
