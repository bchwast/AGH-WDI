def wczytywanie():
    u = tuple(input("> ").split("/"))
    return u


def wypisywanie(u):
    if u[0] == 0:
        return 0
    if u[1] == 1:
        return f"{u[0]}"
    return f"{u[0]}/{u[1]}"


def wspm(u1, u2):
    if u1[1] != u2[1]:
        m = u1[1] * u2[1]
        l1 = u1[0] * u2[1]
        l2 = u2[0] * u1[1]
    else:
        l1 = u1[0]
        l2 = u2[0]
        m = u1[1]
    return (l1,m) , (l2,m)


def suma(u1, u2):
    u1, u2 = wspm(u1, u2)
    u = (u1[0] + u2[0], u1[1])
    return skracanie(u)


def roznica(u1, u2):
    u1, u2 = wspm(u1, u2)
    u = (u1[0] - u2[0], u1[1])
    return skracanie(u)


def iloczyn(u1, u2):
    l = u1[0] * u2[0]
    m = u1[1] * u2[1]
    u = (l,m)
    return skracanie(u)


def iloraz(u1,u2):
    l = u1[0] * u2[1]
    m = u1[1] * u2[0]
    if m < 0:
        l *= -1
        m *= -1
    u = (l,m)
    return skracanie(u)


def potega(u, p):
    l = u[0]**p
    m = u[0]**p
    u = (l,m)
    return u


def skracanie(u):
    l = u[0]
    m = u[1]
    skracac = True
    i = 2
    while i <= l and i <= m:
        while l%i == 0 and m%i == 0:
            l //= i
            m //= i
        i += 1
    #end while
    return (l, m)


if __name__ == "__main__":

    wypisywanie(iloczyn(wczytywanie(),wczytywanie()))