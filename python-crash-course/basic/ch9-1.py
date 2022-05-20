class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over.")


class Cat:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def sit(self):
        print(f"{self.__name} is now sitting.")

    def roll_over(self):
        print(f"{self.__name} rolled over.")

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def aging(self):
        self.__age += 1

my_dog = Dog('welly', 5)
print(my_dog.age)
my_cat = Cat('kitty', 3)
# print(my_cat.age) # __age is private and cannot be referred
print(my_cat.get_age())
my_cat.aging()
print(my_cat.get_age())