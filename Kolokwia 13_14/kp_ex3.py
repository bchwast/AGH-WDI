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

def piatki(num):
    cnt = 0
    while num > 0:
        if num%8 == 5:
            cnt += 1
        num //= 8
    #end while
    if cnt%2 == 1:
        return True
    return False
#end def

def przen(l):
    if not l.first:
        return

    p = None
    r = l.first
    while r:
        if piatki(r.val) and p:
            p.next = r.next
            r.next = l.first
            l.first = r
            r = p.next
        else:
            p = r
            r = r.next
    #end while
#end def


el1 = Node(13)
el1.next = Node(0)
el1.next.next = Node(5)
el1.next.next.next = Node(0)
el1.next.next.next.next = Node(21)
l1 = LL(el1)
wypisz(l1)
przen(l1)
wypisz(l1)