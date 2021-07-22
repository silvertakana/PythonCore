import random
def new_random_list(l):
     mylist = l.copy()
     random.shuffle(mylist)
     return mylist[:5]
print(new_random_list([1,2,3,4,5,6,7,8,9,0]))
