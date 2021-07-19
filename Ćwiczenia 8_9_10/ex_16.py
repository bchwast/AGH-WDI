def ile_samoglosek(s):
    samogloski = "oaeiuy"
    counter = 0
    for let in s:
        if let in samogloski:
            counter += 1
    #end for
    return counter
#end def


def suma_ascii(s):
    suma = 0
    for let in s:
        suma += ord(let)
    return suma
#end def


def sprawdz(wzor, sprawdzany, index=0, obecny=""):
    if ile_samoglosek(wzor) == ile_samoglosek(obecny) and suma_ascii(wzor) == suma_ascii(obecny):
        return True
    if index == len(sprawdzany):
        return False
    return sprawdz(wzor, sprawdzany, index+1, obecny+sprawdzany[index]) or sprawdz(wzor, sprawdzany, index+1, obecny)
#end def


def wyraz(s1, s2):
    return sprawdz(s1, s2)
#end def


print(wyraz("ula","djgjhexe"))