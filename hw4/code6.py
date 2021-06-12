n = float(input("n>>"))
while round(n) != n:
    print("n is not a natural number. try again")
    n = float(input("n>>"))
n = int(n)

for i in range(n+1):
    for j in range(i):
        print(i,end="  ")
    print()
