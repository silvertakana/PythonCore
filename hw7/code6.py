my_list = ["what","why","lol","o","wow"]

# meadthod 1
counter = 0

for i in my_list:
    if len(i) >= 2 and i[0] ==i[-1]:
         counter += 1
print(counter)

# medthod 2

print(len([i for i in my_list if len(i) >= 2 and i[0] ==i[-1]]))
