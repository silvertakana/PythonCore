# get int x
x = float(input("x>>"))
while round(x) != x:
    print("x is not a natural number. try again")
    x = float(input("x>>"))
x = int(x)
# caculate
n=0
z=0
while z<=x:
    n+=1
    z+=n
n-=1
#giving answer
print(f"answer:{int(n)}")
