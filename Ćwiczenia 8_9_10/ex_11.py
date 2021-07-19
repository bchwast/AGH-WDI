licznik = 0
def enki(tab, enka, iloczyn, index=0):
    global licznik
    if enka == 1:
        for i in range(index, len(tab)):
            if tab[i] == iloczyn:
                licznik += 1
    else:
        for i in range(index, len(tab) - enka + 1):
            if iloczyn%tab[i] == 0:
                enki(tab, enka-1, iloczyn//tab[i], i+1)
#end def


enki([4,2,5,2,532,53,23,5,2,54,1,65],4,8)
print(licznik)