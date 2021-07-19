"""N = int(input("> "))

i = 0
for a in range(1,N+1):
    while a%2 == 0:
        a = a//2
    while a%3 == 0:
        a = a//3
    while a%5 == 0:
        a = a//5
    if a == 1:
        i += 1

print(i)
"""
n = int(input("> "))
l = 0

a2 = 1
while a2 <= n:
    a3 = a2
    while a3 <= n:
        a5 = a3
        while a5 <= n:
            l += 1
            a5 *= 5
        a3 *= 3
    a2 *= 2