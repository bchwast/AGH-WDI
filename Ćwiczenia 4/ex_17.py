from math import sqrt


def prime(num):
    if num == 2 or num == 3: return True
    elif num < 2 or num%2 == 0 or num%3 == 0: return False
    i = 5
    while i <= sqrt(num):
        if num%i == 0: return False
        i += 2
        if num%i == 0: return False
        i += 4
    return True


def sumki(tab1, tab2):
    sumy_prime = 0

    mieszanka = []
    for i in range(3**N):
        mieszanka.append([])
        for _ in range(N):
            mieszanka[i].append(0)

    sumy = [0]*(3**N)

    jump_count = 0
    for j in range(N):
        i = 0
        mode = 1
        while i < 3 ** N:
            jump = 3 ** jump_count
            for _ in range(jump):
                if mode == 1:
                    mieszanka[i][j] = tab1[j]
                elif mode == 2:
                    mieszanka[i][j] = tab2[j]
                else:
                    mieszanka[i][j] = (tab1[j] + tab2[j])
                i += 1
            mode += 1
            if mode > 3:
                mode = 1
        jump_count += 1

    for i in range(3**N):
        for j in range(N):
            sumy[i] += mieszanka[i][j]
        if prime(sumy[i]):
            print(sumy[i])
            sumy_prime += 1

    #print(mieszanka)

    return 3**N, sumy_prime


t1 = [1,3,2,4]
t2 = [9,7,4,8]
N = len(t1)
print(sumki(t1,t2))