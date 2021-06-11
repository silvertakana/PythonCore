n = 0.1
while round(n) != n:
    n = float(input("n>>"))
    if(round(n) != n):
        print("n is not a natural number. try again")

n = int(n)
x = float(input("x>>"))

S_1 = 0
for i in range(n+1):
    S_1+=x**i
s1e = (1-x**(n+1))/ (1-x)
print(f"S_1: method 1: {int(S_1)} ; method 2: {int(s1e)}")

S_2 = 0
for i in range(n+1):
    S_2+=(-x)**i    

s2e = (1-(-x)**(n+1))/ (1+x)
print(f"S_2: method 1: {int(S_2)} ; method 2: {int(s2e)}")

def fac(z):
    y = 1
    for i in range(1,z+1):
        y*=i
    return y

S_3 = 0
for i in range(n+1):
    S_3+=(x**i)/ fac(i)


s3e = 1
a = 1
for i in range(1,n+1):
    a=  a*x/i
    s3e = s3e+a
print(f"S_3: method 1: {int(S_3)} ; method 2: {int(s3e)}")
