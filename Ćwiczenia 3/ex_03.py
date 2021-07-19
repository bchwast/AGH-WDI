"""def pali(a):
    a = [i for i in a]
    b = a[::-1]
    if a == b: return True
    return False


def pali2(a):
    a = int(a)
    new_a = []
    while a > 0:
        new_a.append(a%2)
        a = a//2
    if new_a == new_a.reverse(): return True
    return False


x = input("> ")
if pali(x) == True: print("tak")
else: print("nie")
if pali2(x) == True: print("tak")
else: print("nie")"""

"""
x = input("> ")
i = rev_x = 0

for let in x:
    rev_x += int(let)*(10**i)
    i += 1

if int(x) == rev_x: print("palindrom")
else: print("nie palindrom")

x = int(x)
bi_x = rev_bi_x = i = 0
while x > 0:
    rev_bi_x += (x%2)*(10**i)
    x = x//2
    i += 1
print(str(rev_bi_x))
for dig in str(rev_bi_x):
    bi_x += int(dig)*(10**i)
    i += 1

if bi_x == rev_bi_x: print("palindrom dwójkowy")
else: print("nie palindrom dwójkowy")
"""

a = int(input("> "))
b = 0
d = a
while a > 0:
    c = a%10
    a = a//10
    b = b*10 + c

if b == d:
    print("tak")
else:
    print("nie")