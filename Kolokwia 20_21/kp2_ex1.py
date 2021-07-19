# nie mam pojęcia ile pkt

# zakładam int 64 bitowy, czyli każdą liczbę można rozłożyć na mniej niż 100 czynników pierwszych


def factorize(num, tab):
    i = 0
    k = 2
    while num > 1:
        while num % k == 0:
            num //= k
            tab[i] = k
            i += 1
        k += 1

def factors(num_1, num_2, num_3, num_4):
    factors_1 = [None] * 100
    factors_2 = [None] * 100
    factors_3 = [None] * 100
    factors_4 = [None] * 100
    factorize(num_1, factors_1)
    factorize(num_2, factors_2)
    factorize(num_3, factors_3)
    factorize(num_4, factors_4)

    flag = False
    for i in range(100):
        if factors_1[i] is None:
            break
        in_2 = False
        in_3 = False
        in_4 = False

        for j in range(100):
            if factors_2[j] is None:
                break
            if factors_2[j] == factors_1[i]:
                in_2 = True
                break
        if not in_2:
            continue

        for j in range(100):
            if factors_3[j] is None:
                break
            if factors_3[j] == factors_1[i]:
                in_3 = True
                break
        if not in_3:
            continue

        for j in range(100):
            if factors_4[j] is None:
                break
            if factors_4[j] == factors_1[i]:
                in_4 = True
                break
        if not in_4:
            continue

        if flag:
            return False
        flag = True

    return True


def four(T):
    n = len(T)
    cnt = 0

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if factors(T[i - 1][j], T[i + 1][j], T[i][j - 1], T[i][j + 1]):
                cnt += 1

    return cnt
