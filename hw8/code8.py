
from random import randint
import random

def is_element_equal(t1,t2):
    for i in t1:
        if i not in t2: return False
    return True

my_tuple1 = tuple([randint(0,500) for i in range(0,randint(1,30))])
my_tuple2 = tuple([randint(0,500) for i in range(0,randint(1,30))])
my_tuple3 = list(my_tuple1)
random.shuffle(my_tuple3)
my_tuple3 = tuple(my_tuple3)

print(my_tuple1)
print(my_tuple2)
print(my_tuple3)

print(is_element_equal(my_tuple1, my_tuple2))
print(is_element_equal(my_tuple1, my_tuple3))
