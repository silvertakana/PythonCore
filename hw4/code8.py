def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
o_n = input("n>>")
while True:
    if RepresentsInt(o_n):
        n = int(o_n)
        
        if n>0 :
            if n<1000 :
                break
            else :
                print("n is greater than 1000. please try again") 
        else :
            print("n is not a nature number. please try again")  
    else :
        print("n is not an interger. please try again")      
    o_n = input("n>>")

n = int(n)
n = str(n)
z = 0
for i in n:
    z += int(i)
print(z)
