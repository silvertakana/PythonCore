from random import randint
my_dict = dict([(f"element {i}",[randint(0,9) for j in range(randint(5,10))]) for i in range(randint(3,10))])

print(my_dict)

for i in my_dict.values():
	print(i[4])
