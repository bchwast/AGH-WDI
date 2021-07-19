def szachownica(T, k, w=0, result=0):
    result += T[w][k]
    summary = 99999999999999999999999999999999999999
    if w == 7:
        return result
    for i in range(k-1, k+2):
        if i >= 0 and i < 8:
            summary = min(szachownica(T, i, w+1, result), summary)
    #end for
    return summary
#end def


t = [[532,26,25,1,64,24,234,25]]*8
print(szachownica(t,0))
