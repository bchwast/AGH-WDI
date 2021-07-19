class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def insert(first, el):
    p = None
    r = first

    while r is not None and r.val < el:
        p = r
        r = r.next

    new_el = Node(el)

    if p is None:
        new_el.next = r
        return new_el

    new_el.next = r
    p.next = new_el
    return first
#end def


def scal(f_1, f_2):
    first = None
    el_1 = f_1
    el_2 = f_2

    while el_1 is not None:
        first = insert(first, el_1.val)
        el_1 = el_1.next
    while el_2 is not None:
        first = insert(first, el_2.val)
        el_2 = el_2.next

    return first
#end def


def wypisz(first):
    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
#end def


l1 = l2 = None
l1 = insert(l1, 1)
l1 = insert(l1, 4)
l1 = insert(l1, 7)
l2 = insert(l2, 0)
l2 = insert(l2, 2)
l2 = insert(l2, 4)
l2 = insert(l2, 6)
l2 = insert(l2, 5)
wypisz(l1)
print("")
wypisz(l2)
print("")
wypisz(scal(l1,l2))
print("")
wypisz(l1)