class Tab:
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
#end class


class Node:
    def __init__(self, val=None, next=None, index=None):
        self.val = val
        self.next = next
        self.index = index
#end class


def start(n):
    p = Node(None, None, 0)
    T = Tab(p, p)
    for i in range(1, n):
        p = Node(None, None, i)
        T.last.next = p
        T.last = p
    return T
#end def


def insert(T, value, n):
    if n > T.last.index:
        print("index out of range")
        return False
    #end if

    new = Node(value, None, n)

    if n == 0:
        new.next = T.first.next
        T.first = new
        return True
    #end if

    p = None
    r = T.first
    while r is not None:
        if r.index == n:
            new.next = r.next
            p.next = new
            return True
        p = r
        r = r.next
#end def


def read(T, n):
    if n > T.last.index:
        print("index out of range")
        return False
    #end if

    p = T.first
    for i in range(n):
        p = p.next

    return p.val
#end def


def t_print(T):
    p = T.first
    while p is not None:
        print(p.val, end=", ")
        p = p.next
#end def


tab = start(100)