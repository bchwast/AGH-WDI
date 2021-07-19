x = int(input("> "))

a = 1
b = 1
res = 0
fin = False

while a <= x:
    res = a*b
    if res == x:
        print("tak")
        fin = True
        break
    res = 0
    a = a + b
    b = a - b

if fin == False:
    print("nie")