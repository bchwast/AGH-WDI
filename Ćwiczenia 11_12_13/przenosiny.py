from random import randint
class Node:
    def __init__(self,):
        self.right = None
        self.down = None
#end class

w = 5
k = 4

T = [[bool(randint(0,1)) for _ in range(w)] for _ in range(k)]
Tw = [None for _ in range(w)]
Tk = [None for _ in range(k)]

for i in range(w-1, -1, -1):
    for j in range(k-1, -1, -1):
        if T[i][j]:
            p = Node()
            p.right = Tw[i]
            Tw[i] = p
            p.down = Tk[j]
            Tk[j] = p
    #end for
#end for
