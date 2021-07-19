from ex_01 import *
from math import acos, sin, cos, sqrt, pi


def z_wczytywanie():
    re = float(input("re: "))
    im = float(input("im: "))
    return (re,im)


def z_wypisywanie(z):
    if z[0] == int(z[0]):
        re = int(z[0])
    else:
        re = z[0]
    if z[1] == int(z[1]):
        im = int(z[1])
    else:
        im = z[1]
    if re == 0 and im == 0:
        return 0
    elif re == 0:
        return f"{im}i"
    elif im == 0:
        return re
    sgn = " "
    if re > 0:
        sgn = " + "
    elif im < 0:
        sgn = " - "
        im = abs(im)
    return f"{re}{sgn}{im}i"


def z_suma(z1, z2):
    re = z1[0] + z2[0]
    im = z1[1] + z2[1]
    return (re,im)


def z_roznica(z1, z2):
    re = z1[0] - z2[0]
    im = z1[1] - z2[1]
    return (re,im)


def z_iloczyn(z1, z2):
    re = (z1[0]*z2[0] - z1[1]*z2[1])
    im = (z1[0]*z2[1] + z1[1]*z2[0])
    return (re,im)


def z_iloraz(z1, z2):
    m = (z2[0]**2 + z2[1]**2)
    re = (z1[0]*z2[0] + z1[1]*z2[1])
    im = (z1[1]*z2[0] - z1[0]*z2[1])
    re /= m
    im /= m
    return (re,im)


def z_potega(z, p):
    r = sqrt(z[0]**2 + z[1]**2)
    fi = acos(z[0]/r)
    re = (r**p)*cos(p*fi)
    im = (r**p)*sin(p*fi)
    z = (re, im)
    return z


def z_pierwiastek(z):
    print(z)
    r = sqrt(z[0]**2 + z[1]**2)
    if r == 0:
        return (0,0), (0,0)
    fi = acos(z[0]/r)
    re1 = sqrt(r)*cos(fi/2)
    im1 = sqrt(r)*sin(fi/2)
    re2 = sqrt(r)*cos((fi/2) + pi)
    im2 = sqrt(r)*sin((fi/2) + pi)
    z1 = (re1, im1)
    z2 = (re2, im2)
    return z1, z2


if __name__ == "__main__":
    print(z_wypisywanie(z_wczytywanie()))