a = int(input("> "))
b = int(input("> "))
n = int(input("> "))

print(a//b, end=".")
a = a%b

while n > 0:
    a *= 10
    if a > b:
        print(a//b, end="")
        a = a%b
    else:
        print("0", end="")
    n -= 1

