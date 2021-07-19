def jedynki(num):
    ile = 0
    while num > 0:
        if num%2 == 1:
            ile += 1
        num //= 2
    #end for
    return ile
#end def


def check(set1, set2, set3, id1, id2, id3):
    s1 = 0
    for i in range(id1):
        s1 += jedynki(set1[i])
    s2 = 0
    for i in range(id2):
        s2 += jedynki(set2[i])
    s3 = 0
    for i in range(id3):
        s3 += jedynki(set3[i])
    return s1 == s2 == s3
#end def


def podzial(T, set1, set2, set3, id=0, id1=0, id2=0, id3=0):
    if id == len(T):
        if id1 != 0 and id2 != 0 and id3 != 0:
            if check(set1, set2, set3, id1, id2, id3):
                return True
        return False
    #end if
    set1[id1] = T[id]
    if podzial(T, set1, set2, set3, id+1, id1+1, id2, id3):
        return True
    set2[id2] = T[id]
    if podzial(T, set1, set2, set3, id+1, id1, id2+1, id3):
        return True
    set3[id3] = T[id]
    if podzial(T, set1, set2, set3, id+1, id1, id2, id3+1):
        return True
    return False
#end def


def subset(T):
    return podzial(T, [0]*len(T), [0]*len(T), [0]*len(T))
#end def


T = [5, 7, 15]
print(subset(T))
