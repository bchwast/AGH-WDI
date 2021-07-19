x = int(input("> "))

odd = 1
sum = 0
n = 0

while sum <= x:
    sum = sum + odd
    odd = odd + 2
    n = n + 1

print(n-1)