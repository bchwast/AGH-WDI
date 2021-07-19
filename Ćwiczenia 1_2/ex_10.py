"""a = 2

while a < 1000000:
    i = 1
    b = 0 #liczcnik
    while i < a:
        if a%i == 0:
            b += i
        i += 1
    if b == a:
        print(a)
    a += 1"""

a = 1
sum = 1

while 2**a < 1000:
    sum += 2**a
    i = 2
    prime = True
    while i < sum:
        if sum%i == 0:
            prime = False
        i += 1
    if prime == True:
        print(sum*(2**a))
    a += 1


