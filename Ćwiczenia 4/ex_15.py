from random import randint
from math import sqrt

def prime(num):
    if num == 2 or num == 3: return True
    elif num < 2 or num%2 == 0 or num%3 == 0: return False
    i = 5
    while i <= sqrt(num):
        if num%i == 0: return False
        i += 2
        if num%i == 0: return False
        i += 4
    return True

def prog(tab):
    a = 0
    tic = 0
    for i in range(len(t)):
        if i == fibo[a]:
            a += 1
            if prime(tab[i]) == True:
                return False
        else:
            if prime(tab[i]) == True:
                tic += 1
    if tic > 0:
        return True
    return False

fibo = [0 for _ in range(100)]
a = 1
b = 1
for i in range(1,len(fibo)):
    fibo[i] = a
    a = a + b
    b = a - b

t = [randint(0,9999999) for _ in range(2455779)]
print(prog(t))