from math import sqrt
from math import ceil
N = int(input("> "))

tab = [True for _ in range(N+1)]
tab[0] = tab[1] = False

for i in range(2, ceil(sqrt(N) + 1)):
    if tab[i]:
        for a in range(i*i,N+1,i):
            tab[a] = False

for i in range(N+1):
    if tab[i]: print(i)
