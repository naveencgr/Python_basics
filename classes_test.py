class Point:
    def draw(self):
        print("draw")

    def paint(self):
        print("paint")

point1 = Point()
point1.abc = 10
point1.zef = 20 
print(point1.zef)
point1.draw()
point1.paint()


class Person:
    
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} talking")

person = Person("Nav")
person.talk()

