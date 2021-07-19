def sortuj(tabliczka):
    sortowac = True
    while sortowac == True:
        sortowac = False
        for i in range(len(tabliczka)-1):
            if tabliczka[i] < tabliczka[i+1]:
                temp = tabliczka[i]
                tabliczka[i] = tabliczka[i+1]
                tabliczka[i+1] = temp
                sortowac = True
    return tabliczka


temp = int(input("> "))
tab = [0 for _ in range(100)]
n = 0

while temp != 0:
    tab[n] = temp
    temp = int(input("> "))
    n += 1

tab = sortuj(tab)

for i in range(10):
    print(tab[i],end=", ")
