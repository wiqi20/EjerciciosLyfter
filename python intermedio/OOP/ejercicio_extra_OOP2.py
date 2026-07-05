class Animal:
    def __init__(self, name):
        self.name=name

    def speak(self):
        return print("Make's a sound")


class Dog(Animal):
    def speak(self):
        return print(f"{self.name} says, Guau!")


class Cat(Animal):
    def speak(self):
        return print(f"{self.name} says, Miau!")


dog= Dog("Firulais")
cat=Cat("Misingo")

dog.speak()
cat.speak()
