liczba = int(input("> "))

for pdst in range(2,17):
    num = liczba
    new_liczba = 0
    i = 0
    while num > 0:
        new_liczba += (num%pdst)*(10**i)
        if num%pdst >= 10:
            i+=1
        num //= pdst
        i += 1
    print(new_liczba)

"""
from pdst in range(2,17):
    num = liczba
    new_liczba = ""
    i = 0
    while num > 0:
        temp = num%pdst
        if temp >= 10:
            temp = chr(temp + 55)
        new_liczba = str(temp) + new_liczba
        num //= podst
    print(new_liczba)
"""

"""
from math import log
from math import ceil
def zpl(liczba, podstawa):
    hex = "0123456789ABCDEF"
    tab = [0 for _ in range(ceil(log(liczba, podstawa))]
    i = 0
    while liczba > 0:
        tab[i] = liczba%podstawa
        liczba //= podstawa
        i += 1
    tab.reverse()
    for i in tab:
        print(i, end="")
"""