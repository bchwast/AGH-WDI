#napisy składają się tylko z małych liter alfabetu łacińskiego

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


class LL:
    def __init__(self, first=None):
        self.first = first
#end class


def wstaw(l, napis):
    el = Node(napis)
    for let in napis:
        n_k = let
    n_p = napis[0]

    p = None
    r = l.first
    mem = r
    while True:
        p = r
        r = r.next
        if r == mem:
            return False

        s_p = r.val[0]
        for let in p.val:
            s_k = let

        if ord(s_k) < ord(n_p) and ord(n_k) < ord(s_p):
            p.next = el
            el.next = r
            l.first = el
            return True
    #end while
#end def


l = LL()
a = Node("bartek")
b = Node("zosia", a)
c = Node("ola", b)
d = Node("marek", c)
e = Node("leszek", d)
a.next = e
l.first = a
print(l.first.val)
print(wstaw(l, "lom"))
print(l.first.val)

