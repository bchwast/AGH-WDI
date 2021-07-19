from math import sqrt

a = sqrt(0.5)
res = a
i = 0
while i <= 1000:
    a = sqrt(0.5 + 0.5*a)
    res = res*a
    i += 1

print(2/res)