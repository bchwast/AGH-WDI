k = int(input("> "))

a_n = b_n = a_n1 = a_n2 = b_n1 = b_n2 = b_n3 = 1
wart = 0
wyr = 0
while k > wyr:
    if a_n == b_n and a_n != wart:
        wyr += 1
        wart = a_n

    while k > wyr:
        if a_n <= b_n:
            if wart != a_n:
                wart = a_n
                wyr += 1
            a_n = a_n1 + a_n2
            a_n2 = a_n1
            a_n1 = a_n
        else:
            break
    #end while

    while k > wyr:
        if b_n <= a_n:
            if wart != b_n:
                wart = b_n
                wyr += 1
            b_n = b_n1 + b_n2 + b_n3
            b_n3 = b_n2
            b_n2 = b_n1
            b_n1 = b_n
        else:
            break
    #end while
#end while

print(wart)