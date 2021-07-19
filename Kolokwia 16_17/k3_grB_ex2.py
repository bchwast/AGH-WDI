class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
#end class

class LL:
    def __init__(self, first=None):
        self.first = first
#end class

def wypisz(l):
    if not l.first:
        return

    p = l.first
    while p:
        print(p.val, end=" -> ")
        p = p.next
    print()
#end def

def y_lista(l1, l2):
    cnt = 0

    if (not l1.first) or (not l2.first):
        return cnt

    p = None
    r = l1.first
    while r:
        p2 = None
        r2 = l2.first
        while r2 and r2.val != r.val:
            p2 = r2
            r2 = r2.next

        if r2 and r2.val == r.val:
            if p2:
                p2.next = None
            break

        p = r
        r = r.next
    #end def

    while r:
        cnt += 1
        if not p2:
            p2 = Node(r.val)
            l2.first = p2
        else:
            p2.next = Node(r.val)
            p2 = p2.next
        r = r.next
    #end while

    return cnt
#end def


el1 = Node(5)
el1.next = Node(11)
el1.next.next = Node(3)
el1.next.next.next = Node(2)
el2 = Node(65)
el2.next = el1
l1 = LL(el1)
l2 = LL(el2)
wypisz(l1)
wypisz(l2)
print(y_lista(l1, l2))
wypisz(l1)
wypisz(l2)
