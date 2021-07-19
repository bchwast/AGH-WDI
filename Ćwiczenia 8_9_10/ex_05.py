from math import sqrt


def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 or num%3 == 0:
        return False
    i = 5
    while i <= sqrt(num):
        if num%i == 0:
            return False
        i += 2
        if num%i == 0:
            return False
        i += 4
    #end while
    return True
#end def


def ciach(tab, p=0):
    if p == len(tab):
        return True
    num = 0
    for i in range(p, min(len(tab),30)):
        num = num*2 + tab[i]
        if prime(num) and ciach(tab, i+1):
            return True
    #end for
    return False
#end def


print(ciach([1,1,0,1,0,0]))