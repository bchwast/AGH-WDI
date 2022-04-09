t = [0] * 1000

i = 0
while True:
    num = int(input("> "))
    if num != 0:
        t[i] = num
        i += 1
    else:
        break
print('here')
biggest = [float("inf") for _ in range(11)]

for j in range(1, 11):
    max_num = -1
    for k in range(i):
        if t[k] > max_num and t[k] < biggest[j - 1]:
            max_num = t[k]
    biggest[j] = max_num

print(biggest)

print(biggest[10])