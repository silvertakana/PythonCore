
from math import inf
from random import randint

# create the list
the_list = []
for i in range(randint(0,10)):
    the_tuple = tuple([randint(0,500) for i in range(randint(3,10))])
    the_list.append(the_tuple)

# medthod 1

# define sort function
def sorter(t):
    return t[1]

# sort list
the_list.sort(key = sorter)

# print list
print(the_list[0])

# medthod 2
a = inf

for i in the_list:
    if(i[1] < a):
        a = i[1]
        b = i
print(b)
