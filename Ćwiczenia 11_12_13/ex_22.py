class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def czy_cykl(first):
    if not first:
        return False

    if not first.next:
        return False

    slow_p = first
    fast_p = first
    while slow_p and fast_p and fast_p.next:
        slow_p = slow_p.next
        fast_p = fast_p.next.next
        if slow_p == fast_p:
            return True
    #end while

    return False
#end def


g = Node(2)
f = Node(3, g)
e = Node(4, f)
d = Node(5, e)
c = Node(4, d)
b = Node(3, c)
a = Node(2, b)
g.next = c
l1 = a

print(czy_cykl(l1))