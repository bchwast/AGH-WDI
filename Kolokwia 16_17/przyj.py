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

    return l
#end def

def przyjaciolki(num1, num2):
    l1 = do_tablicy(num1)
    l2 = do_tablicy(num2)

    for i in range(len(l1)):
        zawiera = False
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                zawiera = True
        #end for
        if not zawiera:
            return False
    #end for

    for i in range(len(l2)):
        zawiera = False
        for j in range(len(l1)):
            if l2[i] == l1[j]:
                zawiera = True
        #end for
        if not zawiera:
            return False
    #end for

    return True
#end def

def only_f(t):
    N = len(t)
    cnt = 0
    if N == 1:
        return 0

    w = [-1, -1, -1, 0, 1, 1, 1, 0]
    k = [-1, 0, 1, 1, 1, 0, -1, -1]
    for i in range(N):
        for j in range(N):
            friends = True
            for m in range(8):
                if 0 <= i+w[m] < N and 0 <= j+k[m] < N:
                    if not przyjaciolki(t[i][j], t[i+w[m]][j+k[m]]):
                        friends = False
                        break
            #end for
            if friends:
                cnt += 1
        #end for
    #end for

    return cnt
#end def