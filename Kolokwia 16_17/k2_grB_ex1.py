def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 or num%3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2

        if num%i == 0:
            return False
        i += 4
    #end while
    return True
#end def

def sumy(t1, t2):
    wszystkie = wypisane = 0

    def core(t1, t2, suma=0, ind=0):
        nonlocal wszystkie, wypisane
        if ind == len(t1):
            wszystkie += 1
            if prime(suma):
                print(suma)
                wypisane += 1
        else:
            core(t1, t2, suma+t1[ind], ind+1)
            core(t1, t2, suma+t2[ind], ind+1)
            core(t1, t2, suma+t1[ind]+t2[ind], ind+1)
    #end def

    core(t1, t2)

    return wszystkie, wypisane
#end def


t1 = [1,3,2,4]
t2 = [9,7,4,8]
print(sumy(t1, t2))
