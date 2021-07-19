e = 0
fact = 1
for i in range(1,101,1):
    e = e + 1/fact
    fact = fact*i
print(e)