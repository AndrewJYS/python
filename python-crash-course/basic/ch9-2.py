class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def description(self):
        print(f"This animal is called {self.name}, and is {self.age} years old.")

    def rename(self, new_name):
        self.name = new_name

    def aging(self):
        self.age += 1

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")

    def drink(self):
        print(f"{self.name} is drinking.")


class Dog(Animal):

    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def get_height(self):
        return self.height

    def description(self):
        print(f"My dog is called {self.name}.")
        print(f"It is {self.age} years old.")
        print(f"It is {self.height} centimeters high.")


my_dog = Dog('wiley', 6, 60)
print(my_dog.name)
my_dog.description()