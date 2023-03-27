class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f'Name: {self.name}, breed: {self.breed}')


class Person:
    def __init__(self, name, age, gender):
        self.dog = None
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        print(f'Name: {self.name}, age: {self.age}')

    def add_dog(self, dog):
        if not isinstance(dog, Dog):
            raise TypeError("Invalid input")
        self.dog = dog

    def bark(self):
        if self.dog:
            self.dog.bark()
        else:
            print(f"{self.name} doesn't have a dog.")


dog1 = Dog("Arnie", "Pug", 7)
person1 = Person("Andrey", "27", "male")
person1.add_dog(dog1)
person1.bark()
