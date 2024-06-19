class Animal:
    def sound(self):
        print("Sound")

class Cat(Animal):
    def sound(self):
        print("Bark")

class Dog(Animal):
    def sound(self):
        print("Meow")       

cat = Cat()
cat.sound()

dog = Dog()
dog.sound()

animal = Animal()
animal.sound()
