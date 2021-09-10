class Dog:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

class Pet:
    def __init__(self,dogs):
        self.dogs = dogs
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
