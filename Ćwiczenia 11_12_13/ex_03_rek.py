class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def rek_scal(l1, l2):
    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.val < l2.val:
        res = l1
        res.next = rek_scal(l1.next, l2)
    else:
        res = l2
        res.next = rek_scal(l1, l2.next)

    return res
#end def