#zakładam, że napisy składają się tylko z małych liter łacińskiego alfabetu
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


def is_greater(napis_1, napis_2):
    for i in range(max(len(napis_1), len(napis_2))):
        if i >= len(napis_1):
            return False
        if i >= len(napis_2):
            return True
        if ord(napis_1[i]) > ord(napis_2[i]):
            return True
        if ord(napis_1[i]) < ord(napis_2[i]):
            return False
#end def


def insert(first, napis):
    new_napis = Node(napis)

    if not first:
        first = new_napis
        return first

    if is_in(first, napis):
        return first

    if is_greater(first.val, napis):
        new_napis.next = first
        first = new_napis
        return first

    p = None
    r = first
    while r is not None:
        while is_greater(napis, r.val):
            p = r
            r = r.next

    p.next = new_napis
    new_napis.next = r
    return first
#end def


l1 = None
l1 = insert(l1, 'mazik')
l1 = insert(l1, 'gazik')
l1 = insert(l1, 'dziad')
l1 = insert(l1, 'mazik')
wypisz(l1)
