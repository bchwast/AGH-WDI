def an(num):
    a = 2
    while num >= a:
        if num == a: return True
        a = 3*a + 1
    return False


liczba = int(input("> "))

if an(liczba) == True: print("tak")
else: print("nie")
