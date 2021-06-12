n = float(input("n>>"))
while round(n) != n:
    print("n is not a natural number. try again")
    n = float(input("n>>"))
n = int(n)

i = 1
x = 1
while i*3<n:
    x+=i*3
    i+=1
print(x)
