class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
#end class


def scal(f1, f2):
    f = Node()
    l = f
    while f1 is not None and f2 is not None:
        if f1.val < f2.val:
            l.next = f1
            l = f1
            f1 = f1.next
        else:
            l.next = f1
            l = f2
            f2 = f2.next
    #end while
    if f1 != None:
        l.next = f1
    else:
        l.next = f2
    return f.next
#end def