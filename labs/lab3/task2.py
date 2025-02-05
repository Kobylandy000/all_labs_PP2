class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input("Enter l of Square: "))

    def area(self):
        print(self.length * self.length)

class Triangle(Shape):
    def __init__(self):
        self.length = int(input("Enter l of Triangle: "))

    def area(self):
        print(self.length * self.length * 1.71 / 4)

while(True):
    print("[1] create new Shape")
    print("[0] exit")
    choice = int(input())
    if choice == 1:
        s1 = Shape()
        print("[1] create Square")
        print("[2] create Triangle")
        subChoice = int(input())
        if subChoice == 1:
            s1 = Square()
        elif subChoice == 2:
            s1 = Triangle()
        s1.area()
    elif choice == 0:
        break