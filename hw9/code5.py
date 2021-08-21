from random import randint

def key_intersection(d1,d2):
	joined_dict_keys = set(d1) & set(d2)
	print(joined_dict_keys)


my_dict = dict([(f"{randint(0,10)}",randint(0,10000)) for i in range(randint(1,100))])
my_dict2 = dict([(f"{randint(0,10)}",randint(0,10000)) for i in range(randint(1,100))])

print(my_dict)
print(my_dict2)
key_intersection(my_dict,my_dict2)
