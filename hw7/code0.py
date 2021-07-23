import random
def new_random_list(l):
     if(len(l) < 5): 
          print("this list does not have enough element")
          return []
     mylist = l.copy()
     random.shuffle(mylist)
     return mylist[:5]
print(new_random_list([1,2,3,4,5,6,7,8,9,0]))
