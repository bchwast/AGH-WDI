#zakladam, ze liczby w t1 sa mniejsze niz 999999999999999999999999999

def przepisz(t1, t2):
    M = len(t2)
    N = M//10

    ind = 0
    lrgst = 999999999999999999999999999
    while ind < M:
        byl = False
        num = -1
        for i in range(10):
            for j in range(N):
                if t1[i][j] < num:
                    break

                if t1[i][j] < lrgst:
                    if t1[i][j] == num:
                        byl = True
                        break
                    else:
                        num = t1[i][j]
            #end for
        #end for
        if num == -1:
            t2[ind] = 0
            ind += 1
        else:
            lrgst = num
            if not byl:
                t2[ind] = lrgst
                ind += 1
    #end while
#end def

t1 = [[6,4,2,1],[75,43,32,1],[23,12,11,1],[34,21,13,2],[23,13,12,9],[56,34,21,6],[13,12,5,2],[15,3,2,1],[65,34,23,1],[666,32,12,5]]
t2 = [None]*40
przepisz(t1,t2)
print(t2)