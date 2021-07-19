def prime(num):
    if num == 2 or num == 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False

    i = 5
    while i*i <= num:
        if num%i == 0:
            return False
        i += 2
        if num%i == 0:
            return False
        i += 4
    #end while
    return True
#end def

def ciag(t):
    N = len(t)

    #wiersze
    for i in range(N):
        for j in range(N-2):
            if prime(t[i][j]):
                if prime(t[i][j+1]):
                    dl = 2
                    r = t[i][j+1]-t[i][j]
                    ind = j + 2
                    while ind < N:
                        if prime(t[i][ind]) and t[i][ind]-t[i][ind-1] == r:
                            dl += 1
                            ind += 1
                        else:
                            break
                    #end while
                    if dl > 2:
                        return dl
        #end for
    #end for

    #kolumny
    for i in range(N):
        for j in range(N-2):
            if prime(t[j][i]):
                if prime(t[j+1][i]):
                    dl = 2
                    r = t[j+1][i]-t[j][i]
                    ind = j + 2
                    while ind < N:
                        if prime(t[ind][i]) and t[ind][i]-t[ind-1][i] == r:
                            dl += 1
                            ind += 1
                        else:
                            break
                    #end while
                    if dl > 2:
                        return dl
        #end for
    #end for

    return 0
#end def

t = [[4, 3, 7, 5, 10],[6,2,4,5,6],[4,7,7,5,5,2],[3,5,76,3,4],[36,2,5,12,4]]
print(ciag(t))