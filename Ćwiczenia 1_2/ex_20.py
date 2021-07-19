eps = 0.00000000000001

a_n = 2
b_n = 2

while abs(a_n - b_n) > eps:
    a_n_temp = a_n
    a_n = (a_n*b_n)**(0.5)
    b_n = (a_n_temp + b_n)/2

print(a_n)
