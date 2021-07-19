N = int(input("> "))

omega = 365**N
opp_a = 1
for i in range(N):
    opp_a *= (365-i)
p = (omega - opp_a)/omega
print(p)