def podzialy(liczba, s=[], last=1):
    if liczba == 0:
        print(s)
    else:
        for i in range(last, liczba+1):
            podzialy(liczba-i, s+[i], i)
#end def


podzialy(7)
