class Student:
    # Constructor
    def __init__(self):
        print("Creating new object...")

    # Constructor with parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getString(self):
        print("Hello from getString mathod")

s1 = Student("Almas", 18)  # s1 - Student класынын объектісі
s1.getString()