k = int(input("> "))

a_n = 1
b_n = 2
i_a = 1
mem = -99999999999999
while True:
    if a_n == k:
        odl_a = 0
        n_a = i_a
        break
    elif a_n < k:
        mem = k - a_n
        i_a += 1
    else:
        if a_n - k >= k - mem:
            n_a = i_a - 1
            odl_a = mem
        else:
            n_a = i_a
            odl_a = a_n - k
        break
    b_n_1 = b_n
    a_n_1 = a_n
    b_n = b_n_1 + a_n_1
    a_n = a_n_1 + (b_n)/3
#end while

a_n = 1
b_n = 2
i_b = 1
mem = -9999999999
while True:
    if b_n == k:
        odl_b = 0
        n_b = i_b
        break
    elif b_n < k:
        mem = k - b_n
        i_b += 1
    else:
        if b_n - k >= k - mem:
            n_b = i_b - 1
            odl_b = mem
        else:
            n_b = i_b
            odl_b = b_n - k
        break
    b_n_1 = b_n
    a_n_1 = a_n
    b_n = b_n_1 + a_n_1
    a_n = a_n_1 + (b_n)/3
#end while

if odl_a == odl_b:
    if n_a < n_b:
        print("a", n_a)
    else:
        print("b", n_b)
elif odl_a < odl_b:
    print("a", n_a)
else:
    print("b", n_b)