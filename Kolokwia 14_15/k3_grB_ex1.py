def ciag(t):
    N = 1000
    dl_m = 1
    for w in range(N-1):
        for k in range(N-1):
            curr = 2
            q = t[w+1][k+1]/t[w][k]
            w_n = w+2
            k_n = k+2
            while w_n < N and k_n < N and t[w_n][k_n]/t[w_n-1][k_n-1] == q:
                curr += 1
                w_n += 1
                k_n += 1
            #end while
            if curr > dl_m:
                dl_m = curr
        #end for
    #end for
    if dl_m >= 3:
        return dl_m
    return False
#end def