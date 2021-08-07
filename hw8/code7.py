from random import randint

def is_colide(t1,t2):
    for i in t1:
        for j in t2:
            if i == j: return True
    return False

my_tuple1 = tuple([randint(0,500) for i in range(0,randint(1,30))])
my_tuple2 = tuple([randint(0,500) for i in range(0,randint(1,30))])

print(my_tuple1)
print(my_tuple2)

print(is_colide(my_tuple1, my_tuple2))
