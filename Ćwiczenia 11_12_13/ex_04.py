class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def insert_l(first, el):
    p = None
    r = first

    while r is not None:
        p = r
        r = r.next

    new_el = Node(el)

    if p is None:
        return new_el

    p.next = new_el
    return first
#end def


def wypisz(first):
    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
#end def


def reverse(first):
    if first is None:
        return first

    p = None
    r = first
    while r is not None:
        next = r.next
        r.next = p
        p = r
        r = next
    return p
#end def


l1 = l2 = l3 = None
l1 = insert_l(l1, 1)
l1 = insert_l(l1, 4)
l1 = insert_l(l1, 7)
l2 = insert_l(l2, 0)
l2 = insert_l(l2, 2)
l2 = insert_l(l2, 4)
l2 = insert_l(l2, 6)
l2 = insert_l(l2, 5)
l3 = insert_l(l3, 1)
wypisz(l1)
print("")
wypisz(l2)
print("")
wypisz(reverse(l3))