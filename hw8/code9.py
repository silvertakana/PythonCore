from random import uniform

my_numbers = [uniform(0,10000000) for i in range(0,100)]
my_numbers = tuple(my_numbers)
print("Largest element is:", max(my_numbers))

total = 0
for i in range(len(my_numbers)):
    total += my_numbers[i]

print(total)
