class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
#end class

def uni(first):
    if not first:
        return None
    if not first.next:
        return first

    prev = None
    p = first
    while p:
        q = p
        flaga = False
        while q:
            if q.next.val == p.val:
                q.next = q.next.next
                flaga = True
            else:
                q = q.next
        if flaga:
            if not prev:
                first = first.next
                p = first
            else:
                prev.next = p.next
                p = p.next
                pass
        #end while
        else:
            prev = p
            p = p.next
    #end while

    return first
#end def

