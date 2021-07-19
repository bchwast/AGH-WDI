#zakladam, ze w liczby w t1 sa mniejsze niz 99999999999999999999999999999

def przepisz(t1, t2):
    ind = 0
    N = len(t1)
    M = N*N
    lrgst = 99999999999999999999999999999*10
    while ind < M:
        num = -1
        cnt = 1
        for i in range(N):
            for j in range(N):
                if t1[i][j] < num:
                    break

                if t1[i][j] < lrgst:
                    if t1[i][j] > num:
                        cnt = 1
                        num = t1[i][j]
                        break
                    else:
                        cnt += 1
            #end for
        #end for

        lrgst = num
        while cnt > 0:
            t2[ind] = lrgst
            ind += 1
            cnt -= 1
        #end while
    #end while
#end def

t1 = [[7, 4, 3, 1], [523, 3, 1, 1], [23, 13, 6, 2], [23, 15, 4, 2]]
t2 = [None]*16
przepisz(t1, t2)
print(t2)

