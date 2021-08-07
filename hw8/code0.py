from random import uniform

my_tuple = [uniform(0,10000000) for i in range(0,3)]
my_tuple = tuple(my_tuple)

a,b,c = my_tuple
print(my_tuple)
print(a,b,c)
