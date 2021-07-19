liczba = int(input("> "))
num = liczba
digits = 0

while num > 0:
    digits += 1
    num //= 10

dzielnik = 7
counter = 0
for i in range(1,2**digits):
    check = 0
    bin_num = i
    num = liczba
    new_digs = 0
    for j in range(0,digits):
        if bin_num % 2 == 1:
            check += (10**new_digs)*(num%10)
            new_digs += 1
        bin_num //= 2
        num //= 10
    if check % 7 == 0:
        print(check)
        counter += 1

print(f"Jest {counter} takich liczb")