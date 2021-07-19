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

    stop = l.first
    p = l.first
    while True:
        print(p.val, end=" -> ")
        p = p.next
        if p == stop:
            break
    print()
#end def

def powt(l1, l2):
    cnt = 0

    if (not l1.first) or (not l2.first):
        return cnt

    if l1.first == l1.first.next:
        min1 = max1 = l1.first
    else:
        p = l1.first
        r = l1.first.next
        while r.val > p.val:
            p = r
            r = r.next
        max1 = p
        min1 = r
    max1.next = None

    if l2.first == l2.first.next:
        min2 = max2 = l2.first
    else:
        p = l2.first
        r = l2.first.next
        while r.val > p.val:
            p = r
            r = r.next
        max2 = p
        min2 = r
    max2.next = None

    p = None
    r = min1
    while r:
        if r.val < min2.val:
            p = r
            r = r.next
        elif r.val == min2.val:
            cnt += 1
            if p:
                p.next = r.next
                r = r.next
            else:
                min1 = r.next
                r = r.next
            min2 = min2.next
        else:
            p2 = min2
            r2 = min2.next
            while r2 and r.val < r2.val:
                p2 = r2
                r2 = r2.next

            if r2 and r.val == r2.val:
                cnt += 1
                if not p:
                    min1 = min1.next
                else:
                    p.next = r.next
                r = r.next

                p2.next = r2.next
            else:
                p = r
                r = r.next
    #end while

    p1 = None
    r1 = min1
    while r1:
        p1 = r1
        r1 = r1.next
    p1.next = min1

    p2 = None
    r2 = min2
    while r2:
        p2 = r2
        r2 = r2.next
    p2.next = min2

    l1.first = min1
    l2.first = min2

    return cnt
#end def


el1 = Node(5)
el1.next = Node(7)
el1.next.next = Node(9)
el1.next.next.next = Node(3)
el1.next.next.next.next = el1
el2 = Node(8)
el2.next = Node(2)
el2.next.next = Node(3)
el2.next.next.next = el2
l1 = LL(el1)
l2 = LL(el2)
wypisz(l1)
wypisz(l2)
print(powt(l1,l2))
wypisz(l1)
wypisz(l2)