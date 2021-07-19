# Bartłomiej Chwast
# Program sprawdza czy któryś ze zbiorów nie jest pusty, używam wartownika, w pęli while sprawdzam czy element pierwszego
# zbioru znajduje się w pozostałych zbiorach, jeżeli tak to przepinam ten punkt na początek nowej listy (za wartownika)
# zwracam wskaźnik na element po wartowniku

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
#end class

def czy_jest(z, num):
    if not z:
        return False

    p = z
    while p and p.val <= num:
        if p.val == num:
            return True
    #end while
    return False
#end def

def iloczyn(z1, z2, z3):
    if not z1 or not z2 or not z3:
        return None

    WART = Node("!")

    p = None
    r = z1
    while r:
        if czy_jest(z2, r.val) and czy_jest(z3, r.val):
            new_el = Node(r.val)
            new_el.next = WART.next
            WART.next = new_el
        r = r.next
    #end while

    return WART.next
#end def
