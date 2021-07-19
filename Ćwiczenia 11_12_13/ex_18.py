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


def uni(first, el):
    if not first:
        return first

    flaga = False
    p = None
    r = first
    while r is not None:
        if not flaga:
            if r.val == el:
                flaga = True
            p = r
            r = r.next
        else:
            if r.val == el:
                r = r.next
                p.next = r
            else:
                p = r
                r = r.next
    #end while

    return first
#end def


def przegl(first):
    if not first:
        return first

    go = 0
    p = first
    while p is not None:
        first = uni(first, p.val)
        p = p.next

    return first
#end def


l1 = None
l1 = append(l1, 1)
l1 = append(l1, 2)
l1 = append(l1, 2)
l1 = append(l1, 2)
wypisz(l1)
l1 = przegl(l1)
wypisz(l1)

