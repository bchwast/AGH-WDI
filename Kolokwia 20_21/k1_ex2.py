# 5 pkt

def compare(T, a, b):
    i = 0
    while T[a][i] == T[b][i]:
        i += 1

    return T[a][i] > T[b][i]


def distance(T):
    N = len(T)
    i_max = i_min = 0
    for i in range(N):
        if compare(T, i, i_max):
            i_max = i

        if compare(T, i_min, i):
            i_min = i


    return abs(i_max - i_min)

