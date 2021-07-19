def prime(num):
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    return False


def wstaw(t, ind, dig):
    for i in range(ind):
        if t[i] == dig:
            return False

    if abs(t[ind-1] - dig) < 2:
        return False

    if prime(dig) and prime(t[ind-1]):
        return False

    return True
#end def


def rozmieszczenia(t, ind):
    if ind == 8:
        print(t)

    if ind < 8:
        for dig in range(2,10):
            if wstaw(t, ind+1, dig):
                t[ind+1] = dig
                rozmieszczenia(t, ind+1)
#end def


t = [1, 0, 0, 0, 0, 0, 0, 0, 0]
rozmieszczenia(t, 0)
