N = int(input("> "))

for i in range(10**(N-1),10**N):
    n = N
    sum = 0
    i_2 = i
    while n > 0:
        sum += (i_2%10)**N
        i_2 //= 10
        n -= 1
    print(sum)
    if sum == i:
        print(i)

