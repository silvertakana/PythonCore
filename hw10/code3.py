class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def eat(self):
        if self.is_hungry:
            self.is_hungry = False
        else:
            print(f"{self.name} is not hungry!")

class Pet:
    def __init__(self,dogs):
        self.dogs = dogs
    def feed(self):
        feeded = True
        for dog in self.dogs:
            if dog.is_hungry:
                feeded = False
                dog.eat()
        
        if feeded:
            print("My dogs are not hungry.")
            for dog in self.dogs:
                dog.is_hungry = True
        
    def __str__(self):
        s = ""
        s += f"I have {len(self.dogs)} dogs\n"
        for dog in self.dogs:
            s += f"{dog.name} is {dog.age} years old. "
        s += "\nand they are mammals, of course."
        return s

class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

my_pets = Pet([
    Dog("Tom",6),
    Dog("Jerry",9),
    Dog("Butt",3),
    Dog("Wine",1)
])
print(my_pets)

my_pets.feed()
my_pets.feed()
