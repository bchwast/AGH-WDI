class Node:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
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
        print(f"({p.x},{p.y})", end=" -> ")
        p = p.next
    print()
#end def

def rozdziel(l, l1, l2, l3, l4):
    if not l.first:
        return

    r = l.first
    while r:
        new = Node(r.x,r.y)
        if r.x > 0 and r.y > 0:     #I cwiartka
            new.next = l1.first
            l1.first = new
        elif r.x < 0 and r.y > 0:   #II cwiartka
            new.next = l2.first
            l2.first = new
        elif r.x < 0 and r.y < 0:   #III cwiartka
            new.next = l3.first
            l3.first = new
        elif r.x > 0 and r.y < 0:   #IV cwiartka
            new.next = l4.first
            l4.first = new
        l.first = l.first.next
        r = l.first
    #end while
#end def


el1 = Node(5,2)
el1.next = Node(-3,-5)
el1.next.next = Node(32,-4)
el1.next.next.next = Node(9,0)
el1.next.next.next.next = Node(-2, 4)
el1.next.next.next.next.next = Node(2,5)
l = LL(el1)
l1 = LL()
l2 = LL()
l3 = LL()
l4 = LL()
wypisz(l)
wypisz(l1)
wypisz(l2)
wypisz(l3)
wypisz(l4)
rozdziel(l, l1, l2, l3, l4)
wypisz(l)
wypisz(l1)
wypisz(l2)
wypisz(l3)
wypisz(l4)