from random import randint

my_tuple = tuple([randint(0,500) for i in range(0,randint(4,100))])

print(my_tuple)
print(my_tuple[3],my_tuple[-4])
