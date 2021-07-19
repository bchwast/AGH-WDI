#zakladam, ze ciag ma mniej niz 1000 liczb i liczby sa mniejsze od 999999999999999999999999999999999999999999999999

ciag = [0]*1000

i = 0
while True:
    ciag[i] = int(input("> "))
    if ciag[i] == 0:
        break
    else:
        i += 1
#end while

lrgst = 999999999999999999999999999999999999999999999999
for _ in range(10):
    i = 0
    num = -1
    while ciag[i] != 0:
        if ciag[i] > num and ciag[i] < lrgst:
            num = ciag[i]
        i += 1
    #end while
    lrgst = num
#end for

print(lrgst)