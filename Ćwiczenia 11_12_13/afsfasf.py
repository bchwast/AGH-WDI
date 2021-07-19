class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def write(first, el):
    new_el = Node(el)
    new_el.next = first
    first = new_el
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


def rozdz(first):
    def scal():
        first = None
        for i in range(9, -1, -1):
            p = None
            r = l[i]
            while r is not None:
                p = r
                first = write(first, p.val)
                r = r.next
        #end for
        return first

    l = [None]*10
    p = None
    r = first
    while r is not None:
        p = r
        l[p.val%10] = write(l[p.val%10], p.val)
        r = r.next
    for i in range(10):
        wypisz(l[i])

    return scal()
#end def


l1 = None
l1 = write(l1, 53)
l1 = write(l1, 98)
l1 = write(l1, 21)
l1 = write(l1, 3)
l1 = write(l1, 24)
l1 = write(l1, 75)
wypisz(l1)
wypisz(rozdz(l1))