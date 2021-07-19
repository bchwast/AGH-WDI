a = 1
b = 2
suma_a = 0
suma_b = 0

while a < 10**6:
    i = 1
    while i < a:
        if a%i == 0:
            suma_a += i
        i += 1
    while b < 10**6 and b <= suma_a:
        i = 1
        while i < b and suma_b <= a:
            if b%i == 0:
                suma_b += i
            i += 1
        if suma_a == b and suma_b == a:
            print(a, b)
        suma_b = 0
        b += 1
    suma_a = 0
    a += 1
    b = a + 1