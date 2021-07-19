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


l1 = int(input("> "))
l2 = int(input("> "))
l_1 = l1
l_2 = l2

dig1 = 0
while l_1 > 0:
    dig1 += 1
    l_1 //= 10

tl1 = [0 for i in range(dig1)]
tl2 = tl1.copy()

for i in range(dig1):
    tl1[i] = l1%10
    tl2[i] = l2%10
    l1 //= 10
    l2 //= 10

tl1 = sortuj(tl1)
tl2 = sortuj(tl2)

if tl1 == tl2:
    print("są")
else:
    print("nie są")
