mytuple = (1,5,3,65,87,3,23,6)
my2ndtuple = (1,2,3,4,5,6,7,8,9,10)

def is_self_overlap(mytuple):
	for i in range(len(mytuple)):
		if i != mytuple.index(mytuple[i]): return True
	return False

print(is_self_overlap(mytuple))
print(is_self_overlap(my2ndtuple))
