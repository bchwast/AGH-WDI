def ciag(a):
    res = (a%2)*(3*a + 1) + (1 - a%2)*(a/2)
    return res

kroki = 1
maxk = 0
maxl = 0

for i in range(2,10001,1):
    ser = ciag(i)
    while ser != 1:
        kroki += 1
        ser = ciag(ser)
    if kroki > maxk:
        maxk = kroki
        maxl = i
    kroki = 1

print(maxl)