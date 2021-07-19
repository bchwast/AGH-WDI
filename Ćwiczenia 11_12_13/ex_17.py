class Node():
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
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


def jedynki(key):
    il_1 = 0
    while key > 0:
        if key%2 == 1:
            il_1 += 1
        key //= 2

    if il_1%2 == 1:
        return True
    return False
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
    new_el.prev = p
    return first
#end def


def wyczysc(first):
    if not first:
        return first

    p = None
    r = first
    while r is not None:
        if jedynki(r.val):
            if not p:
                r = r.next
                first = r
                if r is not None:
                    r.prev = p
            elif not r.next:
                r = r.next
                p.next = r
            else:
                r = r.next
                r.prev = p
                p.next = r
        else:
            p = r
            r = r.next

    return first
#end def


l1 = None
l1 = append(l1, 1)
l1 = append(l1, 1)
l1 = append(l1, 0)
wypisz(l1)
l1 = wyczysc(l1)
wypisz(l1)

