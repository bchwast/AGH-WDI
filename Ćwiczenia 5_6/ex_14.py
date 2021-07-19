def zgodnel(l1, l2):
    l1c = l1
    l2c = l2
    jed1 = jed2 = 0
    while l1c > 0:
        if l1c%2 == 1:
            jed1 += 1
        l1c //= 2
    while l2c > 0:
        if l2c%2 == 1:
            jed2 += 1
        l2c //= 2
    if jed1 == jed2:
        return True
    return False


def zgodnetab(tab1, tab2):
    N1 = len(tab1)
    N2 = len(tab2)
    warunek = (N1*N1)/3
    for a in range(N2-N1):
        for b in range(N2-N1):
            match = 0
            for i in range(N1):
                for j in range(N1):
                    if zgodnel(tab1[i][j],tab2[a+i][b+j]):
                        match += 1
            if match > warunek:
                return True
    return False
