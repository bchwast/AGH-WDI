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


def poprzedz(first):
    flaga = False
    p = None
    r = first
    while r is not None:
        p = r
        r = r.next
        if r is not None:
            if p.val > r.val:
                p.next = r.next
                flaga = True
    #end while
    if flaga:
        poprzedz(first)

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
l1 = append(l1, 2)
l1 = append(l1, 3)
l1 = append(l1, 15)
l1 = append(l1, 9)
l1 = append(l1, 6)
l1 = append(l1, 13)
wypisz(l1)
l1 = poprzedz(l1)
wypisz(l1)