class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs
    def walk(self):
        for dog in self.dogs:
            dog.walk()

class Dog:
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

    def walk(self):
        print(f"{self.name} is walking at mac 10")

    def eat(self):
        self.is_hungry = False


class RussellTerrier(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'


class Bulldog(Dog):
    def run(self, speed):
        return f'{self.name} runs {speed}'

dogs = Pets([
    Dog("Tom", 0),
    Dog("Jerry", 0),
    Dog("Butt", 0),
    ])
dogs.walk()
