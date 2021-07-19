class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


class LL:
    def __init__(self, first=None):
        self.first = first

    def __str__(self):
        if not self.first:
            return "pusto"

        p = self.first
        while True:
            print(p.val, end=" -> ")
            p = p.next
            if p == self.first:
                break
        return ""

    def delete(self, key, cnt):
        p = self.first
        r = p.next
        while cnt > 0:
            if r.next == r:
                r = None
                break
            if r.val == key:
                p.next = r.next
                r = r.next
                cnt -= 1
            else:
                p = r
                r = r.next
        #end while
        self.first = r
        return
#end class


def usun(l, k):
    first = l.first
    if not first:
        return False

    end = False
    res = False
    while not end:
        end = True
        p = None
        r = l.first
        mem = r
        while True:
            if not l.first:
                end = True
                break

            p = r
            r = r.next

            if mem == r:
                end = True
                break

            cnt = 1
            wzor = r
            while True:
                wzor = wzor.next
                if wzor == r:
                    break
                if wzor.val == r.val:
                    cnt += 1
            if cnt == k:
                res = True
                l.delete(wzor.val, cnt)
                end = False
                break
        #end while
    #end while
    return res
#end def


#end def


l = LL()
a = Node(1)
b = Node(2, a)
c = Node(1, b)
d = Node(2, c)
a.next = d
l.first = a
print(l)
print(usun(l, 2))
print(l)


