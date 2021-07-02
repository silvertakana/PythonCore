t = input("your text>>")
nt = ""
for item in t:
    if(item.upper() == item):
        nt+=item.lower()
    else:
        nt+=item.upper()
print(nt)
