class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_(list_):
    curr = list_
    while curr is not None:
        print(curr.val, end=' -> ')
        curr = curr.next
    print()


def removing(list_, n):
    prev = None
    curr = list_
    while curr:
        if curr.val == n:
            if prev:
                prev.next = curr.next
                break
            else:
                list_.val = list_.next.val
                list_.next = list_.next.next
        prev = curr
        curr = curr.next


def contains_(list_, n):
    curr = list_
    while curr:
        if curr.val == n:
            return True
        curr = curr.next
    return False


def cw_29(list1, list2):
    f1 = list1
    f2 = list2
    deleted = 0
    while f1.next:
        if contains_(list2, f1.val):
            pass
        else:
            removing(list1, f1.val)
            deleted += 1
        f1 = f1.next
    while f2.next:
        if contains_(list1, f2.val):
            pass
        else:
            removing(list2, f2.val)
            deleted += 1
        f2 = f2.next
    return deleted


def write(first, el):
    if not first:
        return Node(el)
    prev = None
    curr = first
    while curr:
        prev = curr
        curr = curr.next
    prev.next = Node(el)
    return first


list1_ = None
list1_ = write(list1_, 2)
list1_ = write(list1_, 4)
list1_ = write(list1_, 5)
list2_ = None
list2_ = write(list2_, 1)
list2_ = write(list2_, 2)
list2_ = write(list2_, 5)

print_(list1_)
print_(list2_)
print(cw_29(list1_, list2_))
print_(list1_)
print_(list2_)