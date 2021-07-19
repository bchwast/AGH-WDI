counter = 0
def composite(num):
    if num <= 3 or num == 5:
        return False
    if num%2 == 0 or num%3 == 0:
        return True
    i = 6
    while i <= num//2:
        if num%(i-1) == 0 or num%(i+1) == 0:
            return True
        i += 6
    return False
#end def


def to_dec(num):
    l = 0
    for i in range(len(num)):
        l = l*2 + num[i]
    return l
#end def


def budowa(A, B, liczba, ind=1):
    global counter
    if A == B == 0 and composite(to_dec(liczba)):
        return True
    else:
        if A > 0:
            liczba[ind] = 1
            if budowa(A-1, B, liczba, ind+1):
                counter += 1
        if B > 0:
            liczba[ind] = 0
            if budowa(A, B-1, liczba, ind+1):
                counter += 1
#end def


def garek(A, B):
    liczba = [None for _ in range(A+B)]
    liczba[0] = 1
    A -= 1
    budowa(A, B, liczba)
    return counter
#end def


print(garek(2,3))
