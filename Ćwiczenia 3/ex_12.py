def cyfry(num):
    copy_num = num
    digits = 1
    while copy_num > 10:
        digits += 1
        copy_num = copy_num//10
    for dig in str(num):
        if int(dig) == digits: return True
    return False


liczba = int(input("> "))

if cyfry(liczba) == True: print("tak")
else: print("nie")