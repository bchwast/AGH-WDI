# Bartłomiej Chwast
# Zadanie 4. pomocnicze sprawdzanie liczb pierwszych, rekurencyjne dokładanie do podziału lub robienie nowego


def prime(num):
    if num == 2 or num == 3:
        return True
    if num < 2 or num%2 == 0 or num%3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
        if num%i == 0:
            return False
        i+= 4
    #end while

    return True
#end def


def podzi(num1, num2=0, podz=1, pot=0):
    if prime(num1) and prime(num2) and prime(podz):
        return True

    if num1 == 0:
        return False

    if num2 == 0 and podzi(num1//10, num2+((num1%10)*(10**pot)), podz, pot+1):
        return True
    if num2 != 0 and podzi(num2, num2%10, podz+1, 0):
        return True

    return False
#end def


def divide(N):
    return podzi(N)
#end def
