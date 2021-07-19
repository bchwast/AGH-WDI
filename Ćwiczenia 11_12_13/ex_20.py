class Node():
    def __init__(self, left=None, right=None, next=None):
        self.left = left
        self.right = right
        self.next = next
#end class


def wypisz(first):
    if not first:
        return
    p = first
    while p is not None:
        print(f"[{p.left},{p.right}] -> ", end="")
        p = p.next
    print("")
#end def


def append(first, left, right):
    el = Node(left, right)
    if not first:
        return el

    p = None
    r = first
    while r is not None:
        p = r
        r = r.next

    p.next = el
    return first
#end def


def redukuj(first):
    if not first:
        return first

    p = None
    r = first
    s = first
    while r is not None:
        p = r
        r = r.next
        while r is not None:
            if p.left <= r.left:
                if r.left <= p.right and r.right >= p.right:    #p r p r
                    p.right = r.right
                    r = r.next
                    s.next = r
                elif r.left <= p.right and r.right <= p.right:    #p r r p
                    r = r.next
                    s.next = r
                else:
                    s = s.next
                    r = r.next
            elif r.left <= p.left:
                if p.left <= r.right and p.right >= r.right:    #r p r p
                    p.left = r.left
                    r = r.next
                    s.next = r
                elif p.left <= r.right and p.right <= r.right:  #r p p r
                    p.left = r.left
                    p.right = r.right
                    r = r.next
                    s.next = r
                else:
                    s = s.next
                    r = r.next
            else:
                s = r
                r = r.next

        s = p.next
        r = s
    #end while
    return first
#end def



l1 = None
l1 = append(l1, 15, 19)
l1 = append(l1, 2, 5)
l1 = append(l1, 7, 11)
l1 = append(l1, 8, 12)
l1 = append(l1, 5, 6)
l1 = append(l1, 13, 17)
l1 = append(l1, 27, 30)
l1 = append(l1, 25, 27)
wypisz(l1)
l1 = redukuj(l1)
wypisz(l1)