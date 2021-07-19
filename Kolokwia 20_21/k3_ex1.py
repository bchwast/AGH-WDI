# 5 pkt

def nwd(a, b):
    while b != 0:
        b, a = a % b, b

    return a


def trojki(T):
    N = len(T)
    cnt = 0
    for i in range(N - 2):
        for j in range(i + 1, i + 3, 1):
            if j < N:
                for k in range(j + 1, j + 3, 1):
                    if k < N and nwd(T[i], T[j]) == nwd(T[j], T[k]) == nwd(T[i], T[k]) == 1:
                        cnt += 1

    return cnt


# def trojki(T):
#     N = len(T)
#     cnt = 0
#     for i in range(N - 2):
#         for j in range(i + 1, i + 3, 1):
#             if j < N:
#                 for k in range(j + 1, j + 3, 1):
#                     if k < N and nwd(nwd(T[i], T[j]), T[k]) == 1:
#                         cnt += 1
#
#     return cnt
