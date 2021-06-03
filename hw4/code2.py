a = float(input("a>>"))
b = float(input("b>>"))
c = float(input("c>>"))

if a > 0 and b > 0 and c > 0 :
    print("number accepted")
    isposible = (a+b)>c and (a+c)>b and (c+b)>a
    if isposible :
        word = "possible"
    else :
        word = "not posible"
    print(f"this triangle is {word}")
else :
    print("number can't be negative!")
