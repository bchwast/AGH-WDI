class Klocek:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
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
        print(f"[{p.a}|{p.b}]", end=" ")
        p = p.next
    print()
#end def

def ustaw(l):
    if not l.first:
        return

    p = None
    r = l.first
    while r:
        start = True
        p1 = None
        r1 = l.first
        while r1:
            if not r1 == r:
                if r.a == r1.b:
                    start = False
                    break
            p1 = r1
            r1 = r1.next
        #end while
        if start:
            if p:
                p.next = r.next
                r.next = l.first
                l.first = r
            break
        p = r
        r = r.next
    #end while

    p = None
    r = l.first
    while r:
        p1 = None
        r1 = l.first
        while r1:
            if not r1 == r:
                if r.b == r1.a:
                    p1.next = r1.next
                    r1.next = r.next
                    r.next = r1
                    break
            p1 = r1
            r1 = r1.next
        p = r
        r = r.next
    #end while
#end def


el1 = Klocek(2,9)
el1.next = Klocek(3,6)
el1.next.next = Klocek(8,2)
el1.next.next.next = Klocek(2,3)
el1.next.next.next.next = Klocek(6,2)
l1 = LL(el1)
wypisz(l1)
ustaw(l1)
wypisz(l1)