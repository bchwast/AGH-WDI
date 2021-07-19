target = int(input("> "))

a = 1
b = 1
sum = b
end = False

while sum <= target:
    f1 = a
    f2 = b
    while sum <= target:
        if sum == target:
            print("taki ciąg istnieje")
            end = True
            break
        else:
            sum = sum + f1
            f1 = f1 + f2
            f2 = f1 - f2
    if end == True:
        break
    a = a + b
    b = a - b
    sum = b

if end == False:
    print("taki ciąg nie istnieje")