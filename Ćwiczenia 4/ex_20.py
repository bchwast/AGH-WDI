from random import randint


def podciag(tab):
    len_new = 1
    len_m = 1
    for i in range(N-1):
        if tab[i]%tab[i+1] != 0:
            len_new += 1
            temp = tab[i+1]*tab[i]
            for j in range(i+1,N-1):
                if temp%tab[j+1] != 0:
                    len_new += 1
                    temp *= tab[j+1]
                else:
                    break
        print(i,len_new)
        if len_new > len_m:
            len_m = len_new
        len_new = 1
    print(len_m)


#N = int(input("> "))
#t = [randint(1,999) for _ in range(N)]
t = [2,23,33,35,7,4,6,7,5,11,13,22]
N = len(t)
podciag(t)