def change_upper_lower1(str):
    ns = ""
    for i in range(len(str)):
        s = str[i]
        if(s.isupper()):
            ns += str[i].lower()
        else:
            ns += str[i].upper()
    return ns

def change_upper_lower2(str):
    return str.swapcase()
print(change_upper_lower2("Hello World!"))
