
from random import randint

# create the list
the_list = []
for i in range(randint(0,10)):
    the_tuple = tuple([randint(0,500) for i in range(randint(1,4))])
    the_list.append(the_tuple)

# define sort function
def sorter(t):
    return t[-1]

# sort list
the_list.sort(key = sorter)

# print list
print(the_list)
