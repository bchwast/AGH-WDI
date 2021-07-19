def nwd(num1, num2):
    while num2 != 0:
        num2, num1 = num1%num2, num2

    return num1
#end def


def wzgl_pierwsze(num1, num2, ind1, ind2):
    n1 = n2 = 0
    i = 0
    ind1 -= 1
    while ind1 >= 0:
        n1 += num1[i]*(10**ind1)
        ind1 -= 1
        i += 1

    i = 0
    ind2 -= 1
    while ind2 >= 0:
        n2 += num2[i]*(10**ind2)
        ind2 -= 1
        i += 1

    if nwd(n1, n2) == 1:
        return n1, n2
    return None
#end def


def rozbicia(n):
    c_n = n
    l = 0
    while c_n > 0:
        l += 1
        c_n //= 10
    num = [0]*l
    for i in range(l-1, -1, -1):
        num[i] = n%10
        n //= 10

    licznik = 0

    def core(n, a, b, ind_a=0, ind_b=0, ind_n=0):
        nonlocal licznik
        if ind_n == len(n):
            if ind_a > 0 and ind_b > 0:
                liczba = wzgl_pierwsze(a, b, ind_a, ind_b)
                if liczba is not None:
                    print(liczba)
                    licznik += 1
        else:
            a[ind_a] = n[ind_n]
            core(n, a, b, ind_a + 1, ind_b, ind_n + 1)

            b[ind_b] = n[ind_n]
            core(n, a, b, ind_a, ind_b + 1, ind_n + 1)
    # end def

    core(num, [0]*l, [0]*l)
    return licznik
#end def


print(rozbicia(21523))