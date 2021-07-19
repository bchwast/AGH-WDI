def can_it(target, r):
    if len(r) < 3:
        return False
    if r[0] + r[1] + r[2] == target:
        return True
    if (r[0]*r[1]*r[2])/(r[0]*r[1] + r[0]*r[2] + r[1]*r[2]) == target:
        return True
    if ((r[0] + r[1])*r[2])/(r[0] + r[1] + r[2]) == target:
        return True
    if ((r[0] + r[2])*r[1])/(r[0] + r[1] + r[2]) == target:
        return True
    if (r[0]*r[1])/(r[0] + r[1]) + r[2] == target:
        return True
    if (r[0]*r[2])/(r[0] + r[2]) + r[1] == target:
        return True
    if (r[1]*r[2])/(r[1] + r[2]) + r[0] == target:
        return True
    return False
#end def


def opor(T, omega, zestaw, ile=3, index=0):
    if ile == 0:
        if can_it(omega, zestaw):
            return True
    elif ile < 4:
        for i in range(index, len(T) - ile + 1):
            zestaw[3-ile] = T[i]
            if opor(T, omega, zestaw, ile-1, i+1):
                return True
    return False
#end def


t = [1, 25, 87, 50, 34, 42]
print(opor(t, 76, [0,0,0]))