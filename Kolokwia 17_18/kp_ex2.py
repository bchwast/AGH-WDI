def pary(t1, t2):
    def wycinanie(tab1, tab2, istart, jstart, suma1, suma2, ile1, ile2):
        N = len(tab1)
        if ile2 == 0:
            for j in range(jstart, N):
                print("suma1:", suma1, "suma2:", suma2)
                if suma2 == suma1:
                    return N - wyc
            return 0
        #end if
        if ile1 == 0:
            for j in range(jstart, N-1):
                suma2_n = suma2 - tab2[j]
                if wycinanie(tab1, tab2, istart, j, suma1, suma2_n, ile1, ile2-1) == N-wyc:
                    return N-wyc
        #end if
        if ile1 > 0:
            for i in range(istart, N-1):
                suma1_n = suma1 - tab1[i]
                if wycinanie(tab1, tab2, i, jstart, suma1_n, suma2, ile1-1, ile2) == N-wyc:
                    return N-wyc
    #end def


    N = len(t1)
    suma1 = suma2 = 0
    for i in range(N):
        suma1 += t1[i]
        suma2 += t2[i]
    #end for
    print("suma1z:", suma1,"suma2z:", suma2)
    for wyc in range(N):
        suma1_t = suma1
        suma2_t = suma2
        if wycinanie(t1, t2, 0, 0, suma1_t, suma2_t, wyc, wyc) == N-wyc:
            return N - wyc
    #end for
    return 0
#end def


t1 = [1,2,3,4]
t2 = [5,6,1,1]
print(pary(t1,t2))

