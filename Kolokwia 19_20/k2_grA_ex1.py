def parz5(num):
    cnt = 0
    while num > 0:
        if (num%5)%2 == 0:
            cnt += 1
        num //= 5
    #end while
    return cnt
#end def

def przykrywanie(tab1, tab2):
    MAX1 = len(tab1)
    MAX2 = len(tab2)
    w = [-1, -1, -1, 0, 1, 1, 1, 0, 0]
    k = [-1, 0, 1, 1, 1, 0, -1, -1, 0]

    for i2 in range(MAX2):
        for j2 in range(MAX2):
            cnt = 0
            for ind in range(9):
                if i2 + w[ind] >= 0 and i2 + w[ind] < MAX2
