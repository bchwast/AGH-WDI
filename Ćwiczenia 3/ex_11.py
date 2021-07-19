def ciag(num):
    prev = 0
    for dig in num:
        if prev >= int(dig): return False
        prev = int(dig)
    return True


liczba = input("> ")

if ciag(liczba) == True: print("rosnący")
else : print("nierosnący")
