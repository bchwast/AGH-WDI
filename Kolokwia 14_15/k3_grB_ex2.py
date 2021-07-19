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
    cnt = 0

    while l1.first and l2.first:
        if l1.first.val < l2.first.val:
            cnt += 1
            l1.first = l1.first.next
        elif l2.first.val < l1.first.val:
            cnt += 1
            l2.first = l2.first.next
        else:
            break
    #end while

    if not l1.first:
        while l2.first:
            cnt += 1
            l2.first = l2.first.next
        return cnt
    if not l2.first:
        while l1.first:
            cnt += 1
            l1.first = l1.first.next
        return cnt

    p1 = l1.first
    r1 = l1.first.next
    p2 = l2.first
    r2 = l2.first.next
    while r1 and r2:
        if r1.val == r2.val:
            p1 = r1
            r1 = r1.next
            p2 = r2
            r2 = r2.next
        elif r1.val < r2.val:
            cnt += 1
            p1.next = r1.next
            r1 = r1.next
        elif r2.val < r1.val:
            cnt += 1
            p2.next = r2.next
            r2 = r2.next
    #end while
    if r1:
        cnt += 1
        p1.next = None
    elif r2:
        cnt += 1
        p2.next = None
    return cnt
#end def


el1 = Node(3)
el1.next = Node(5)
el1.next.next = Node(13)
l1 = LL(el1)
el2 = Node(2)
el2.next = Node(3)
el2.next.next = Node(5)
el2.next.next.next = Node(7)
l2 = LL(el2)
wypisz(l1)
wypisz(l2)
print(powt(l1, l2))
wypisz(l1)
wypisz(l2)
