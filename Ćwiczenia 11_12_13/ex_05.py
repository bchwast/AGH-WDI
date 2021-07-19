class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
#end class


def split(head):
    first = [None for _ in range(10)]
    last = [None for _ in range(10)]

    while head is not None:
        c = head.val%10
        if first[c] is None:
            first[c] = last[c] = head
        else:
            last[c].next = head
            last[c] = last[c].next
        head = head.next
    #end while

    result = None
    for i in range(9, -1, -1):
        if first is not None:
            last[i].next = result
            result = first[i]
    #end for

    return result
#end def