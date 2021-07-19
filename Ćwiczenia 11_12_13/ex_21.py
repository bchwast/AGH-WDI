class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def wypisz(first):
    if not first:
        return
    p = first
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("")
#end def


def append(first, el):
    new_el = Node(el)
    if not first:
        return new_el

    p = None
    r = first
    while r is not None:
        p = r
        r = r.next

    p.next = new_el
    return first
#end def


def podlista(first):
    if not first or not first.next:
        return None

    flaga = False
    dl_m = 1
    dl_curr = 1
    p = None
    r = first
    while r is not None:
        p = r
        r = r.next
        cp = p
        cr = r
        while cr is not None:
            if cr.val > cp.val:
                dl_curr += 1
                cp = cr
                cr = cr.next
            else:
                if dl_m == dl_curr:
                    flaga = False
                    dl_curr = 1
                    break
                elif dl_curr > dl_m:
                    flaga = True
                    dl_m = dl_curr
                    dl_curr = 1
                    mem = p
                    break
                else:
                    dl_curr = 1
                    break
        if dl_m == dl_curr:
            flaga = False
            dl_curr = 1
        elif dl_curr > dl_m:
            flaga = True
            dl_m = dl_curr
            dl_curr = 1
            mem = p
        else:
            dl_curr = 1
    #end while

    if flaga:
        a = None
        b = first
        while b != mem:
            a = b
            b = b.next
        while dl_m > 0:
            if not a:
                b = b.next
                first = b
            else:
                b = b.next
                a.next = b
            dl_m -= 1
    #end if

    return first
#end def


l1 = None
l1 = append(l1, 1)
l1 = append(l1, 2)
l1 = append(l1, 3)
l1 = append(l1, 1)
l1 = append(l1, 2)
wypisz(l1)
l1 = podlista(l1)
wypisz(l1)


