def df(x):
    return (x**x)*(log10(x)+1)

def x0(x):
    return (x**x - 2020 - df(x)*x)/(-1*df(x))

from math import log10

eps = 0.000001
c_new = 4
c = 5

while abs(c - c_new) > eps:
    c = c_new
    c_new = c - (c**c - 2020)/df(c)

print(c)
