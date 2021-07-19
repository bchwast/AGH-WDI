from ex_06 import *


def rownanie(a, b, c):
    print(z_potega(b,2))
    print(z_iloczyn((4,0),z_iloczyn(a,c)))
    delta = z_roznica(z_potega(b,2),z_iloczyn((4,0),z_iloczyn(a,c)))
    print(delta)
    p1_delta, p2_delta = z_pierwiastek(delta)
    z1 = z_iloraz(z_roznica(p1_delta,b),z_iloczyn((2,0),a))
    z2 = z_iloraz(z_roznica(p2_delta,b),z_iloczyn((2,0),a))
    return z1, z2


print(rownanie((1,0),(-2,0),(1,0)))
