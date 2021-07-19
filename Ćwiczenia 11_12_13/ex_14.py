class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def wypisz(first):
    if not first:
        return

    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("")
#end def


def dziel(first):
    flaga = False

    if not first:
        return first
    if not first.next:
        return first

    p = first
    r = first.next
    while r is not None:
        if r.val%p.val == 0:
            flaga = True
            bye = p
            break
        p = r
        r = r.next
    if flaga:
        p = None
        r = first
        while r != bye:
            p = r
            r = r.next
        if p is not None:
            p.next = r.next
        else:
            r.next = r.next.next
        return dziel(first)

    return first
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
l1 = append(l1, 3)
l1 = append(l1, 3)
l1 = append(l1, 5)
wypisz(l1)
l1 = dziel(l1)
wypisz(l1)