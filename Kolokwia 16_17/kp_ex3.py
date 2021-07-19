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

def powt(l1, l2, l3):
    cnt = 0
    if not l1.first or not l2.first or not l3.first:
        return cnt

    p1 = None
    r1 = l1.first
    while r1:
        p2 = None
        r2 = l2.first
        is_in3 = False
        while r2:
            if r1.val < r2.val:
                break
            elif r1.val == r2.val:
                p3 = None
                r3 = l3.first
                while r3:
                    if r1.val < r3.val:
                        break
                    elif r1.val == r3.val:
                        cnt += 1
                        is_in3 = True
                        if not p3:
                            l3.first = l3.first.next
                        else:
                            p3.next = r3.next
                        break
                    else:
                        p3 = r3
                        r3 = r3.next
                #end while
                if is_in3:
                    if not p2:
                        l2.first = l2.first.next
                    else:
                        p2.next = r2.next
                break
            else:
                p2 = r2
                r2 = r2.next
        #end while
        if is_in3:
            if not p1:
                l1.first = l1.first.next
            else:
                p1.next = r1.next
        else:
            p1 = r1
        r1 = r1.next
    #end while

    return cnt
#end def


el1 = Node(1)
el1.next = Node(2)
el1.next.next = Node(5)
el2 = Node(5)
el3 = Node(1)
el3.next = Node(5)
el3.next.next = Node(7)
l1 = LL(el1)
l2 = LL(el2)
l3 = LL(el3)
wypisz(l1)
wypisz(l2)
wypisz(l3)
print(powt(l1, l2, l3))
wypisz(l1)
wypisz(l2)
wypisz(l3)