# 5 pkt

def longest(T):
    n = len(T)
    res = 2

    for i in range(n - 2):
        tmp = 2
        if T[i][0] == 0 or T[i + 1][1] == 0:
            continue
        q = (T[i + 1][0] / T[i + 1][1]) * (T[i][1] / T[i][0])
        j = i + 2

        while j < n and T[j - 1][0] != 0 and T[j][1] != 0 and (T[j][0] / T[j][1]) * (T[j - 1][1] / T[j - 1][0]) == q:
            tmp += 1
            j += 1

        res = max(res, tmp)

    if res == 2:
        return 0
    return res
