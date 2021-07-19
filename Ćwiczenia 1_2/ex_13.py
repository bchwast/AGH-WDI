a = int(input("> "))
b = int(input("> "))
c = int(input("> "))
mem_c = c

if a < b:
    temp = a
    a = b
    b = temp
mem_a = a
mem_b = b

while b != 0:
    temp = a
    a = b
    b = temp%b
nwd_a_b = a
nww_a_b = (mem_a*mem_b)//nwd_a_b
nww1 = nww_a_b

if nww_a_b < c:
    temp = nww_a_b
    nww_a_b = c
    c = temp

while c != 0:
    temp = nww_a_b
    nww_a_b = c
    c = temp%c

nwd_a_c = nww_a_b
nww = (nww1*mem_c)//nwd_a_c

print(nww)
