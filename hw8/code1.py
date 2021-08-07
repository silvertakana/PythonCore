
from random import uniform

my_list = [uniform(0,10000000) for i in range(0,3)]
my_tuple = tuple(my_list)

my_2ndlist = list(my_tuple)

print(my_list)
print(my_tuple)
print(my_2ndlist)
