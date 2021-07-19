from random import randint

def powiedz(tab):
    for i in range(len(tab)):
        temp = tab[i]
        while temp > 0:
            if (temp%10)%2 == 0:
                break
            temp //= 10
        else:
            return False
    return True


N = int(input("> "))
t = [randint(1,1000) for _ in range(N)]
print(powiedz(t))