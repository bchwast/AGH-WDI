"""fact = 1
tab = [0 for i in range(1000)]
for i in range(2,1000):
    fact *= i
    temp = 10
    for j in range(1000):
        if temp > 0:
            tab[j] += temp//fact
            if j > 0:
                if tab[j] > 9 and tab[j-1] == 9:
                    tab[j] = tab[j]%10
                    tab[j-1] = 0
                    tab[j-2] += 1
                if tab[j] > 9:
                    tab[j] = tab[j]%10
                    tab[j-1] += 1
        temp %= fact
        temp *= 10
print(2, end=".")
for i in range(1000):
    print(tab[i], end="")
"""

n = 1000
silnia = 1
i = 1
to_add = [0]*n
result = [0]*n
empty = [0]*n

while to_add != empty :
    to_add = [0]*n
    licznik = 1
    to_add[0] = licznik//silnia
    licznik = licznik%silnia
    for a in range(1,n):
        licznik *= 10
        if licznik > silnia:
            to_add[a] = licznik//silnia
            licznik %= silnia
        else:
            to_add[a] = 0
    for a in range(n-1,-1,-1):
        result[a] += to_add[a]
        if result[a] > 9:
            result[a-1] += (result[a]//10)
            result[a] %= 10
    silnia = silnia*i
    i += 1

print(result[a],end=".")
for a in range(1,n):
    print(result[a],end="")