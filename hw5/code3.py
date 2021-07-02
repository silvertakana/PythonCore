t = input("your text>>")
min_char = t[0]

for item in t:
     if item<min_char:
        min_char = item

print(min_char)
