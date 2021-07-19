# 5 pkt

def wielokrotny(napis):
    n = len(napis)
    for d in range(1, n // 2 + 1):
        if n % d == 0:
            if napis[:d] * (n // d) == napis:
                return n

    return 0


def multi(T):
    N = len(T)
    dl_m = 0
    for i in range(N):
        dl_m = max(dl_m, wielokrotny(T[i]))

    return dl_m

