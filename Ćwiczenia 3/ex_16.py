def sum_of_digits(num):
    digits = 0
    while num > 0:
        digits += num%10
        num //= 10
    return digits

for i in range (10000):
    sum_i = sum_of_digits(i)
    a = 2
    sum_a = 0
    i_2 = i
    while a <= i//2:
        while i_2 % a == 0:
            i_2 //= a
            sum_a += sum_of_digits(a)
        a += 1
    if sum_i == sum_a:
        print(i)