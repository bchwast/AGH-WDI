class Nset:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
#end class


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def is_in(nset, el):
    p = nset.first
    while p is not None:
        if p.val == el:
            return True
        p = p.next
    #end while
    return False
#end def


def append(nset, el):
    if is_in(nset, el):
        return False
    q = Node(el)
    if nset.first == None:
        nset.first = q
        nset.last = q
        return True
    nset.last.next = q
    nset.last = q
    return True
#end def


def delete(nset, el):
    if nset.first == None:
        return False
    if nset.first.val == el:
        nset.first = nset.first.next
        return True
    #end if
    p = None
    r = nset.first
    while r is not None:
        if r.val == el:
            p.next = r.next
            if r == nset.last:
                nset.last = p
            return True
        p = r
        r = r.next
    #end while
    return False
#end def


def wypisz(nset):
    p = nset.first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
#end def


nset = Nset()
append(nset, 2)
append(nset, 1)
delete(nset, 1)
wypisz(nset)
