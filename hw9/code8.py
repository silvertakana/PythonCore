your_string = input("enter your string>> ")

all_char = set(your_string)

output = dict([(i,your_string.count(i)) for i in all_char])

print(output)
