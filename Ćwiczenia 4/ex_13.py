from random import randint

N = int(input("> "))
t = [randint(100,999) for _ in range(N)]

l_max = 0
for i in range(len(t)):
    for j in range(len(t)-1,-1,-1):
        if t[i] == t[j]:
            tempi = i
            tempj = j
            ln = 0
            while tempi < len(t) and tempj >= 0:
                if t[tempi] == t[tempj]:
                    ln += 1
                else:
                    break
                tempi += 1
                tempj -= 1
            if ln > l_max:
                l_max = ln
print(l_max)
