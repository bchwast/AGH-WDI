def prime(num):
    if num == 2 or num == 3:
        return True
    elif num < 2 or num%2 == 0 or num%3 == 0:
        return False

    a = 5
    while a*a <= num:
        if num%a == 0:
            return False
        a += 2
        if num%a == 0:
            return False
        a += 4
    #end while
    return True
#end def

def skoki(t, ind=0, cnt=0):
    if ind == (len(t) - 1):
        return cnt

    for i in range(1, len(t)-ind):
        if prime(i) and i < t[ind] and t[ind]%i == 0:
            jump = skoki(t, ind+i, cnt+1)
            if jump > 0:
                return jump
    #end for
    return -1
#end def

t = [25,6,3,7,3,33,5,2,9,5,2,2]
print(skoki(t))
