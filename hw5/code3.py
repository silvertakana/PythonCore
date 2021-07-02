t = input("your text>>")
min_char = t[0]
print(min_char)
for item in t:
     if item<min_char:
        min_char = item

print(min_char)
