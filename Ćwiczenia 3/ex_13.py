def uni(num):
    copy_num = num
    counter = 0
    l_dig = num%10
    for dig in str(num):
        if int(dig) == l_dig: counter += 1
        if counter > 1: return False
    return True

liczba = int(input("> "))

if uni(liczba) == True: print("tak")
else: print("nie")