from math import sqrt

def prime(a):
    i = 2
    if a == 2 or a == 3: return True
    elif a <= 1 or a%2 == 0 or a%3 == 0: return False
    while i <= sqrt(a):
        if a//i == 0: return False
        i += 1
    return True


def prog(n1, n2):
    


liczba1 = int(input("> "))
liczba2 = int(input("> "))

l1 = liczba1
l2 = liczba2
dl_1 = 1
dl_2 = 1
while l1 > 10:
    dl_1 += 1
    l1 = l1//10
while l2 > 10:
    dl_2 += 1
    l2 = l2//10
