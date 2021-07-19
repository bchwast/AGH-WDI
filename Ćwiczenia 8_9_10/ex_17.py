from math import sqrt


licznik = 0


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


def buduj(l1, l2, ktora, nowa=0):
    global licznik
    if ktora == 1:
        nowa *= 10
        nowa += int(str(l1)[0])
        l1 -= int(str(l1)[0])*(10**(len(str(l1))-1))
    else:
        nowa *= 10
        nowa += int(str(l2)[0])
        l2 -= int(str(l2)[0])*(10**(len(str(l2))-1))
    if l1 != 0:
        buduj(l1, l2, 1, nowa)
    if l2 != 0:
        buduj(l1, l2, 2, nowa)
    if len(str(nowa)) == dl:
        if prime(nowa):
            licznik += 1
#end def


def budowanie(l1, l2):
    global dl
    dl = len(str(l1)+str(l2))
    buduj(l1,l2,1)
    buduj(l1,l2,2)
    return licznik
#end def


print(budowanie(2115,69))