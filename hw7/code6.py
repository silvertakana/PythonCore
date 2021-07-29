my_list = ["what","why","lol","o","wow"]

counter = 0

for i in my_list:
    if len(i) >= 2 and i[0] ==i[-1]:
         counter += 1
print(counter)
