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


def inkr(first, rek=0, dalej=None):
    if rek == 0:
        p = None
        r = first
        while r is not None:
            p = r
            r = r.next

        p.val += 1
        if p.val == 10:
            p.val = 0
            return inkr(first, 1, p)
        return first
    #end if

    if rek == 1:
        p = None
        r = first
        while r is not dalej:
            p = r
            r = r.next

        if not p:
            el = Node(1)
            el.next = first
            first = el
            return first
        #end if

        p.val += 1
        if p.val == 10:
            p.val = 0
            return inkr(first, 1, p)

        return first
    #end if
#end def


l1 = None
l1 = append(l1, 4)
l1 = append(l1, 9)
l1 = append(l1, 9)
l1 = inkr(l1)
wypisz(l1)