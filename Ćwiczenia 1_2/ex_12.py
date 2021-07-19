a = int(input("> "))
b = int(input("> "))
c = int(input("> "))

if a < b:
    temp = a
    a = b
    b = temp

while b != 0:
    temp = a
    a = b
    b = temp%b

if a < c:
    temp = a
    a = c
    c = temp

while c != 0:
    temp = a
    a = c
    c = temp%c

print("nwd = ", a)