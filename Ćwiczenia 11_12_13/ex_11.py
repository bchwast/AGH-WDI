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


def is_in(first, key):
    p = first
    while p is not None:
        if p.val == key:
            return True
        p = p.next
    return False
#end def


def klucze(first, key):
    if is_in(first, key):
        if first.val == key:
            first = first.next
            return first

        p = None
        r = first
        while r.val != key:
            p = r
            r = r.next
        p.next = r.next
        return first
    else:
        el = Node(key)
        el.next = first
        first = el
        return first
#end def


l1 = None
l1 = klucze(l1, 2)
l1 = klucze(l1, 3)
l1 = klucze(l1, 6)
l1 = klucze(l1, 2)
l1 = klucze(l1, 6)
wypisz(l1)