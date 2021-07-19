class Node:
    def __init__(self, wyk=None, wsp=None, next=None):
        self.wyk = wyk
        self.wsp = wsp
        self.next = next
#end class


def wypisz(first):
    if not first:
        return

    p = first
    while p:
        print(f"{p.wsp}x^{p.wyk}", end=" + ")
        p = p.next
    print("")
#end def


def append(first, wsp, wyk):
    el = Node(wyk, wsp)
    if not first:
        return el

    if first.wyk > wyk:
        el.next = first
        first = el
        return first

    p = None
    r = first
    while r and r.wyk < wyk:
        p = r
        r = r.next

    p.next = el
    return first
#end def


def odejmij(first, wsp, wyk):
    el = Node(wyk, -1*wsp)
    if not first:
        return el

    if first.wyk > wyk:
        el.next = first
        first = el
        return first

    p = None
    r = first
    while r and r.wyk <= wyk:
        p = r
        r = r.next
        if p.wyk == wyk:
            p.wsp -= wsp
            return first
        if p.wyk < wyk < r.wyk:
            p.next = el
            el.next = r
    #end while

    p.next = el
    return first
#end def


def roznica(f_1, f_2):
    first = None
    x = f_1
    while x:
        first = append(first, x.wsp, x.wyk)
        x = x.next

    p = f_2
    while p:
        first = odejmij(first, p.wsp, p.wyk)
        p = p.next

    return first
#end def


f = None
g = None
f = append(f, 1, 2)
f = append(f, 4, 3)
f = append(f, 2, 1)
f = append(f, 42, 98)
g = append(g, 5, 1)
g = append(g, 11, 4)
g = append(g, 2, 98)
wypisz(f)
wypisz(g)
h = roznica(f, g)
wypisz(h)