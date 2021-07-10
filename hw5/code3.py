t = input("your text>>")
min_char = t[0]
max_char = t[0]

for item in t:
    if item<min_char:
      min_char = item
    if item>max_char:
      max_char = item

print(f"min_char: {min_char}")
print(f"max_char: {max_char}")
