class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def member(zb, e):
    p = first
    while p is not None:
        if p.val == e:
            return True
        p = p.next
    return False


def insert(first, e):
    if member(first, e):
        return

    p = None
    r = first
    while r is not None and r.val < e:
        p = r
        r = r.next

    new_e = Node(e)

    if p is None:
        new_e.next = r
        return new_e

    new_e.next = r
    p.next = new_e
    return first

