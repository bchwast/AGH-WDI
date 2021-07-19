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


def dod(f_1, f_2, first=None, el=0, b1=0, b2=0):
    p1 = None
    p2 = None
    r1 = f_1
    r2 = f_2
    while r1 is not None and r1 and r1 != b1 and b1 is not None:
        p1 = r1
        r1 = r1.next
    while r2 is not None and r2 and r2 != b2 and b2 is not None:
        p2 = r2
        r2 = r2.next
    if p1 is not None:
        el += p1.val
    if p2 is not None:
        el += p2.val
    if el == 0:
        return first

    new_el = Node(el%10)
    new_el.next = first
    first = new_el
    return dod(f_1, f_2, first, el//10, p1, p2)
#end def


l1 = l2 = None
l1 = append(l1, 9)
l2 = append(l2, 9)
l2 = append(l2, 9)
l2 = append(l2, 9)
l3 = dod(l1, l2)
wypisz(l3)
