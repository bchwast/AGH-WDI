from math import pi

x = pi/2
n = 80
i = 1
res = 1
while i <= n:
    j = 1
    fact = 1
    while j <= 2*i:
        fact = fact*j*(j+1)
        j += 2
    res += (((-1)**i)*(x**(2*i)))/fact
    i += 1

print(res)
