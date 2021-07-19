# 5 pkt

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def repair(p):
    head = Node("|")
    head.next = p
    r = p.next.val - p.val

    curr = p.next
    prev = p
    while curr is not None:
        tmp = curr.val - prev.val
        if tmp > 0:
            r = min(r, tmp)
        elif tmp < 0:
            r = max(r, tmp)
        else:
            r = 0
        prev = curr
        curr = curr.next

    cnt = 0
    prev = p
    curr = p.next
    while curr is not None:
        if curr.val - prev.val == r:
            prev = curr
            curr = curr.val
        else:
            new = Node(prev.val + r, curr)
            prev.next = new
            prev = new
            cnt += 1

    return head.next, cnt
