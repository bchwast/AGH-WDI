def ile25(n):
    licznik2 = 0
    while n%2 == 0:
        licznik2 += 1
        n //= 2

    licznik5 = 0
    while n%5 == 0:
        licznik5 += 1
        n //= 5

    return max(licznik2, licznik5)
#end def


licznik = int(input("> "))
mianownik = int(input("> "))

print(licznik//mianownik, end="")
reszta = licznik%mianownik
if reszta > 0:
    print(".", end="")
    for i in range(ile25(mianownik)):
        reszta *= 10
        print(reszta//mianownik, end="")
        reszta %= mianownik
    #end for
    if reszta > 0:
        print("(", end="")
        mem = reszta
        while True:
            reszta *= 10
            print(reszta//mianownik, end="")
            reszta %= mianownik
            if reszta == mem:
                break
        #end while
        print(")")
#end if