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


def remove(first):
    if not first:
        return first

    if not first.next:
        return first.next

    p = None
    q = first
    r = first.next
    while r is not None:
        p = q
        q = r
        r = r.next

    p.next = None
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
l1 = append(l1, 4)
l1 = append(l1, 6)
l1 = remove(l1)
wypisz(l1)


