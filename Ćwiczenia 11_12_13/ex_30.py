class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def wypisz(first):
    if not first:
        return

    p = first
    while p:
        print(p.val, end=" -> ")
        p = p.next
    print("")
#end


def append(first, el):
    new_el = Node(el)
    if not first:
        return new_el

    p = None
    r = first
    while r:
        p = r
        r = r.next

    p.next = new_el
    return first
#end def


def suma(f_1, f_2):
    first = None
    x = f_1
    while x:
        first = append(first, x.val)
        x = x.next

    p = f_2
    while p:
        if p.val < first.val:
            temp = Node(p.val)
            temp.next = first
            first = temp
        p = p.next
    #end while

    curr = f_2
    while curr:
        p = first
        r = first.next
        if p.val == curr.val:
            curr = curr.next
            continue
        while r:
            if p.val < curr.val < r.val:
                temp = Node(curr.val)
                p.next = temp
                temp.next = r
                break
            p = r
            r = r.next
        if not r:
            if p.val < curr.val:
                temp = Node(curr.val)
                p.next = temp
        curr = curr.next
    #end while

    return first
#end def


l1 = None
l2 = None
l1 = append(l1, 2)
l1 = append(l1, 3)
l1 = append(l1, 5)
l1 = append(l1, 7)
l1 = append(l1, 11)
l2 = append(l2, 8)
l2 = append(l2, 2)
l2 = append(l2, 7)
l2 = append(l2, 4)
l2 = append(l2, 1)
l2 = append(l2, 0)
l2 = append(l2, 12)
wypisz(l1)
wypisz(l2)
l3 = suma(l1, l2)
wypisz(l3)



