# 5 pkt

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def czy_jest(z, num):
    if not z:
        return False

    p = z
    while p and p.val <= num:
        if p.val == num:
            return True

    return False


def iloczyn(z1, z2, z3):
    if not z1 or not z2 or not z3:
        return None

    head = Node("|")
    tail = head

    r = z1
    while r:
        if czy_jest(z2, r.val) and czy_jest(z3, r.val):
            tail.next = r
            tail = tail.next
        r = r.next
    tail.next = None

    return head.next
