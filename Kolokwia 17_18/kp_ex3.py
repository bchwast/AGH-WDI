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

def powt(l1, l2):
    lista = LL()

    if (not l1.first) or (not l2.first):
        return lista

    p = None
    r = l1.first
    while r:
        if r.val < l2.first.val:
            p = r
            r = r.next
        elif r.val == l2.first.val:
            num = Node(r.val)
            num.next = lista.first
            lista.first = num
            if not p:
                l1.first = l1.first.next
            else:
                p.next = r.next
            r = r.next
            l2.first = l2.first.next
        else:
            p2 = None
            r2 = l2.first
            while r2 and r2.val < r.val:
                p2 = r2
                r2 = r2.next

            if r2 and r2.val == r.val:
                num = Node(r.val)
                num.next = lista.first
                lista.first = num
                p.next = r.next
                r = r.next
                p2.next = r2.next
            else:
                p = r
                r = r.next
    #end while

    return lista
#end def

el1 = Node(1)
el1.next = Node(3)
el1.next.next = Node(5)
el1.next.next.next = Node(9)
el2 = Node(1)
el2.next = Node(3)
el2.next.next = Node(5)
el2.next.next.next = Node(8)
l1 = LL(el1)
l2 = LL(el2)
wypisz(l1)
wypisz(l2)
l3 = powt(l1, l2)
wypisz(l1)
wypisz(l2)
wypisz(l3)


