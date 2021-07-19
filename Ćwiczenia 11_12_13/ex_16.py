class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def piatki(el):
    il = 0
    while el > 0:
        if el%8 == 5:
            il += 1
        el //= 8

    if il%2 == 0:
        return True
    return False
#end def


def poczatek(first):
    if not first:
        return first

    p = first
    r = first.next
    while r is not None:
        if piatki(r.val):
            p.next = r.next
            r.next = first
            first = r
            r = p.next
        else:
            p = r
            r = r.next


    return first
#end def


def wypisz(first):
    if not first:
        return

    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("")
#end def


def append(first, el):
    new_el = Node(el)
    if not first:
        return new_el

    p = None
    r = first
    while r is not None:
        p = r
        r = r.next

    p.next = new_el
    return first
#end def


l1 = None
l1 = append(l1, 1)
l1 = append(l1, 45)
l1 = append(l1, 45)
wypisz(l1)
l1 = poczatek(l1)
wypisz(l1)