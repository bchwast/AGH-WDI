def do_tablicy(num):
    c_num = num
    dl = 0
    while c_num > 0:
        dl += 1
        c_num //= 10

    l = [None]*dl
    for i in range(dl-1, -1, -1):
        l[i] = num%10
        num //= 10

    fin = [-1]*dl
    ind = 0
    for i in range(dl):
        rep = False
        for j in range(dl):
            if l[i] == fin[j]:
                rep = True
        #end for
        if not rep:
            fin[ind] = l[i]
            ind += 1
    #end for
    return fin
#end def

def kolezanki(num1, num2):
    l1 = do_tablicy(num1)
    l2 = do_tablicy(num2)

    cnt = 0
    for i in range(len(l1)):
        if l1[i] != -1:
            for j in range(len(l2)):
                if l2[j] != -1:
                    if l1[i] == l2[j]:
                        cnt += 1
            #end for
    #end for

    if cnt >= 2:
        return True
    return False
#end def

def zeruj(t):
    N = len(t)
    zero = 0
    for i1 in range(N):
        for j1 in range(N):
            cnt = 0
            for i2 in range(N):
                for j2 in range(N):
                    if i1 != i2 and j1 != j2:
                        if kolezanki(t[i1][j1], t[i2][j2]):
                            cnt += 1
                #end for
            #end for
            if cnt == 0:
                zero += 1
                t[i1][j1] = 0
        #end for
    #end for

    return N*N - zero
#end def

print(kolezanki(2434,643))