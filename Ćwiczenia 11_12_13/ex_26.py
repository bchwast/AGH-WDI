class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
#end class


def czy_zawiera(f_1, f_2):
    if not f_1 or not f_2:
        return True

    check_1 = f_1
    temp = f_2
    while check_1:
        jest = False
        while True:
            if check_1.val == temp.val:
                jest = True
                break
            if temp.next:
                temp = temp.next
            else:
                break
        if jest:
            temp = f_2
            check_1 = check_1.next
        else:
            break
    #end while

    if jest:
        return True

    check_2 = f_2
    temp = f_1
    while check_2:
        jest = False
        while True:
            if check_2.val == temp.val:
                jest = True
                break
            if temp.next:
                temp = temp.next
            else:
                break
        if jest:
            temp = f_1
            check_2 = check_2.next
        else:
            break
    #end while

    if jest:
        return True
    return False
#end def

def append(first, el):
    new_el = Node(el)
    if not first:
        return new_el

    p = None
    r = first
    while r is not None:
        p = r
        r = r.next

    p.next = new_el
    return first
#end def


l1 = None
l2 = None
l1 = append(l1, 1)
l1 = append(l1, 2)
l2 = append(l2, 10)
l2 = append(l2, 11)
l2 = append(l2, 12)
l2 = append(l2, 1)
l2 = append(l2, 2)
print(czy_zawiera(l1, l2))