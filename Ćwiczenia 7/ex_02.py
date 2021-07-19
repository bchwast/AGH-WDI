from ex_01 import *


def uklad(a1, b1, s1, a2, b2, s2):
    wyzn_gl = roznica(iloczyn(a1,b2),iloczyn(b1,a2))
    wyzn_x = roznica(iloczyn(s1,b2),iloczyn(b1,s2))
    wyzn_y = roznica(iloczyn(a1,s2),iloczyn(s1,a2))
    if wyzn_gl[0] == 0:
        if wyzn_x[0] == wyzn_y[0] == 0:
            return "układ nieoznaczony"
        return "układ sprzeczny"
    x = skracanie(iloraz(wyzn_x,wyzn_gl))
    y = skracanie(iloraz(wyzn_y,wyzn_gl))
    return f"x = {wypisywanie(x)}, y = {wypisywanie(y)}"


print("Podaj współczynniki a1, b1, s1, a2, b2, s2 układu równań postaci:\n"
      "a1*x + b1*y = s1\na2*x + b2*y = s2")
print("a1: ",end=" ")
a1 = wczytywanie()
print("b1: ",end=" ")
b1 = wczytywanie()
print("s1: ",end=" ")
s1 = wczytywanie()
print("a2: ",end=" ")
a2 = wczytywanie()
print("b2: ",end=" ")
b2 = wczytywanie()
print("s2: ",end=" ")
s2 = wczytywanie()

print(uklad(a1, b1, s1, a2, b2, s2))
#print(uklad((1,1),(2,1),(7,1),(2,1),(-1,1),(1,1)))