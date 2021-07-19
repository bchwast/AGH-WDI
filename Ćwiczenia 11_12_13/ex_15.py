class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def dwoj_jed(key):
    key_2 = key_1 = key
    il_2 = il_1 = 0

    while key_2 > 0:
        if key_2%3 == 2:
            il_2 += 1
        key_2 //= 3

    while key_1 > 0:
        if key_1%3 == 1:
            il_1 += 1
        key_1 //= 3

    return il_1 > il_2
#end def


def remove(first, el):
    if first.val == el:
        first = first.next
        return first

    p = first
    r = first.next
    while r.val != el:
        p = p.next
        r = r.next
    p.next = r.next
    return first
#end def


def usuw(first):
    p = first
    while p is not None:
        if dwoj_jed(p.val):
            bye = p.val
            first = remove(first, bye)
            return usuw(first)
        p = p.next
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
l1 = append(l1, 1)
l1 = append(l1, 1)
l1 = append(l1, 2)
l1 = append(l1, 1)
l1 = append(l1, 1)
l1 = append(l1, 1)
wypisz(l1)
l1 = usuw(l1)
wypisz(l1)
