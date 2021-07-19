class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def ostatni(first):
    if not first:
        return first

    slow_p = first
    fast_p = first
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            mem = fast_p
            break
    #end while

    p = None
    r = first
    while r != mem:
        p = r
        r = r.next
        mem = mem.next

    return p
#end def


g = Node(2)
f = Node(3, g)
e = Node(4, f)
d = Node(5, e)
c = Node(6, d)
b = Node(7, c)
a = Node(8, b)
g.next = d
l1 = a

print(ostatni(l1).val)