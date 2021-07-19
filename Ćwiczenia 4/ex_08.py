from math import sqrt

def prog(tab):
    i = 2
    num = tab[0]
    while i < sqrt(tab[0]):
        if num%i == 0:
            num //=i
        if i == (len(tab) - 1):
            return True
        i += 1
    return False

t = [30,2,3,1,0,0,0]
print(prog(t))