# zakladam, ze ciag ma mniej niz 1000 liczb

ciag = [0]*1000

i = 0
while True:
    ciag[i] = int(input("> "))
    if ciag[i] == 0:
        break
    else:
        i += 1
#end while

i -= 1
ind = 0
while ind <= i:
    if ind == 0:
        sr = (ciag[1] + ciag[2] + ciag[3] + ciag[4])/4
    elif ind == 1:
        sr = (ciag[0] + ciag[2] + ciag[3] + ciag[4])/4
    elif ind == i:
        sr = (ciag[i-1] + ciag[i-2] + ciag[i-3] + ciag[i-4])/4
    elif ind == i-1:
        sr = (ciag[i] + ciag[i-2] + ciag[i-3] + ciag[i-4])/4
    else:
        sr = (ciag[ind-2] + ciag[ind-1] + ciag[ind+1] + ciag[ind+2])/4

    if sr == ciag[ind]:
        print(ciag[ind])

    ind += 1
#end while