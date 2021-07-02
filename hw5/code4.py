t = input("your text>>")
# medthod 1
nt = ""
for item in t:
    if(item.upper() == item):
        nt+=item.lower()
    else:
        nt+=item.upper()
print(nt)

# medthod 2
nt = t.swapcase()
print(nt)
