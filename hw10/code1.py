class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

dogs = []
dogs.append(Dog("Fake",2))
dogs.append(Dog( "Mickey",7))
dogs.append(Dog("Fuk",5))
def get_oldest_dog(*args):
	"""find the oldest dog"""
	oldest_dog = args[0]
	for d in args:
		if(d.age > oldest_dog.age):
			oldest_dog = d
	return oldest_dog

print(f"The oldest dog is {get_oldest_dog(dogs[0],dogs[1],dogs[2]).age} years old.")
