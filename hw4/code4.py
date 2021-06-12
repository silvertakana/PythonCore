n = float(input("n>>"))
while round(n) != n:
    print("n is not a natural number. try again")
    n = float(input("n>>"))
n = int(n)

x=0
for i in range(n+1):
    x+=i

z= (1+n)*(n)/2
print(f"aswer: method1: {int(x)}; method2: {int(z)}")
