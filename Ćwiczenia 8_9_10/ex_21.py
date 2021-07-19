def mozna(T, wybrane, ind):
    for i in wybrane:
        if i//len(T) == ind//len(T) or i%len(T) == ind%len(T):
            return False
    return True
#end def


def subset(T, suma, s_curr, wybrane, ind):
    if suma == s_curr:
        return True
    elif s_curr > suma:
        return False
    elif ind == (len(T)**2)+1:
        return False

    if mozna(T, wybrane, ind):
        wybrane.append(ind)
        if subset(T, suma, s_curr+T[ind//len(T)][ind%len(T)], wybrane, (ind//len(T))+1):
            return True
        wybrane.pop()
    return False
#end def


def garek(T, suma):
    return subset(T, suma, 0, [], 0)
#end def
