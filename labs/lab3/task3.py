class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = int(input("Enter l: "))
        self.width = int(input("Enter w: "))

    def area(self):
        print(self.width * self.length)

class Square(Shape):
    def __init__(self):
        self.length = int(input("Enter l of Square: "))

    def area(self):
        print(self.length * self.length)

r1 = Rectangle()
r1.area()