def co_najmniej_2(num):
    i = 2
    while num**2 >= i:
        j = i**2
        while num >= j:
            if num == j:
                return True
            j *= i
        i += 1
    return False
#end def


def wycinanie(t1, t2):
    n = len(t1)
    for dl_wyc1 in range(1, 24):
        end1 = n-dl_wyc1+1
        for start1 in range(end1):
            dl_wyc2 = 24 - dl_wyc1
            suma1 = 0
            for el1 in range(start1, start1+dl_wyc1):
                suma1 += t1[el1]

            end2 = n-dl_wyc2+1
            for start2 in range(end2):
                suma2 = 0
                for el2 in range(start2, start2+dl_wyc2):
                    suma2 += t2[el2]

                suma = suma1 + suma2
                if co_najmniej_2(suma):
                    return True
            #end for
        #end for
    #end for
    return False
#end def

t1 = [2 ,3 ,4, 5, 2, 6, 2, 5, 2, 5, 2, 6, 5, 3, 3, 6, 7, 3, 6, 1, 6, 8, 3, 6, 5, 7]
t2 = [4 ,3, 3, 8, 3, 6, 2, 3, 4, 21, 3, 4, 3, 4, 9, 3, 9, 3, 2, 7, 4, 9, 3, 7, 4, 6]
print(wycinanie(t1, t2))


