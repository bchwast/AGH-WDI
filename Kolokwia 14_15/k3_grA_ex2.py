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
    if not l1.first or not l2.first:
        return 0

    cnt = 0
    p = None
    r = l2.first
    while r and l1.first:
        ruch = False
        if r.val < l1.first.val:
            p = r
            r = r.next
        elif r.val == l1.first.val:
            cnt += 1
            if not p:
                l2.first = l2.first.next
            else:
                p.next = r.next
            r = r.next
            l1.first = l1.first.next
        else:
            p1 = l1.first
            r1 = l1.first.next
            while r1:
                if r1.val == r.val:
                    ruch = True
                    cnt += 1
                    p1.next = r1.next
                    r1 = r1.next
                    if not p:
                        l2.first = l2.first.next
                    else:
                        p.next = r.next
                    r = r.next
                elif r1.val < r.val:
                    p1 = r1
                    r1 = r1.next
                else:
                    break
            #end while
            if not ruch:
                p = r
                r = r.next
    #end while
    return cnt
#end def


el1 = Node(3)
el1.next = Node(5)
el1.next.next = Node(7)
el1.next.next.next = Node(9)
el1.next.next.next.next = Node(15)
el2 = Node(15)
el2.next = Node(9)
el2.next.next = Node(3)
l1 = LL(el1)
l2 = LL(el2)
wypisz(l1)
wypisz(l2)
print(powt(l1,l2))
wypisz(l1)
wypisz(l2)