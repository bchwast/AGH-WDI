class Node:
    def __init__(self, val=None, next=None):
        self.val= val
        self.next = next
#end class


class LL:
    def __init__(self, first=None):
        self.first = first

    def __str__(self):
        p = self.first
        if not p:
            return "pusto"
        ret = ""
        while p:
            ret += f"{p.val} -> "
            p = p.next
        return ret

    def insert(self, el):
        new_el = Node(el)
        if not self.first:
            self.first = new_el
            return

        p = None
        r = self.first
        while r:
            p = r
            r = r.next

        p.next = new_el
        return
#end class


def rozdziel(l, l1, l2):
    if not l.first:
        return 0
    cnt = 0
    p = None
    r = l.first
    while r:
        if r.val > 0 and r.val%2 == 0:
            l1.insert(r.val)
            if not p:
                l.first = r.next
                r = r.next
            else:
                p.next = r.next
                r = r.next
        elif r.val < 0 and r.val%2 == 1:
            l2.insert(r.val)
            if not p:
                l.first = r.next
                r = r.next
            else:
                p.next = r.next
                r = r.next
        else:
            cnt += 1
            if not p:
                l.first = r.next
                r = r.next
            else:
                p.next = r.next
                r = r.next
    #end while

    return cnt
#end def


l = LL()
l1 = LL()
l2 = LL()
l.insert(2)
l.insert(3)
l.insert(-5)
l.insert(-6)
print(l)
print(rozdziel(l, l1, l2))
print(l2)

