def i_sum(a, b): return i_short((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))

def i_diff(a, b): return i_short((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))

def i_mul(a, b): return i_short((a[0] * b[0], a[1] * b[1]))

def i_div(a, b): return i_short((a[0] * b[1], a[1] * b[0]))

def i_input(s): return i_short(tuple(map(int, input(s).split("/"))))

def i_pow(a, n): return i_short((a[0]**n),(a[1]**n))

def i_eq(a, b): return a[0]*b[1] == a[1]*b[0]

def i_short(n):
    def nwd(n1, n2):
        n1 = abs(n1)
        n2 = abs(n2)
        while n2 != 0:
            n2, n1 = n1%n2, n2
        return n1
    #end def
    nw = nwd(n[0],n[1])
    return n[0]//nw, n[1]//nw


a = i_input("a: ")
b = i_input("b: ")
c = i_input("c: ")
d = i_input("d: ")
e = i_input("e: ")
f = i_input("f: ")

W = i_diff(i_mul(a,e),i_mul(b,d))
Wx = i_diff(i_mul(c,e),i_mul(f,b))
Wy = i_diff(i_mul(a,f),i_mul(d,c))
x = i_div(Wx,W)
y = i_div(Wy,W)

print(x,y)