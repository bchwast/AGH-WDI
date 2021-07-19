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

def podlista(l):
    if not l.first:
        return 0

    if not l.first.next:
        return 0

    p = l.first
    r = l.first.next
    longest = 1
    start = None
    while r:
        if r.val == p.val:
            mem = p
            current = 2
            p = r
            r = r.next
            while True:
                if r and r.val == p.val:
                    current += 1
                else:
                    if current > longest:
                        longest = current
                        start = mem
                    elif current == longest:
                        start = None
                    break

                p = r
                r = r.next
            #end while
        #end if

        if r:
            p = r
            r = r.next
        else:
            break
    #end while

    if not start:
        return 0

    result = longest

    if start == l.first:
        while longest > 0:
            l.first = l.first.next
            longest -= 1
        return result

    p = None
    r = l.first
    while r != start:
        p = r
        r = r.next

    while longest > 0:
        p.next = r.next
        r = r.next
        longest -= 1

    return result
#end def

l = Node(3)
l.next = Node(3)
l.next.next = Node(2)
l.next.next.next = Node(2)
l.next.next.next.next = Node(2)
f = LL(l)
wypisz(f)
print(podlista(f))
wypisz(f)