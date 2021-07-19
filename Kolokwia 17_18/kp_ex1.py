def kawalki(t):
    N = len(t)
    kawalki_max = 0
    suma = 0
    for i in range(N):
        suma += t[i]
        ind = i + 1
        kawalki_curr = 1
        suma_t = 0
        while ind < N:
            suma_t += t[ind]
            if suma_t == suma:
                suma_t = 0
                kawalki_curr += 1
            ind += 1
        #end while
        if kawalki_curr > 1 and kawalki_curr > kawalki_max and suma_t == 0:
            kawalki_max = kawalki_curr
    #end for
    return kawalki_max
#end def


t = [-45,40,-5]
print(kawalki(t))
