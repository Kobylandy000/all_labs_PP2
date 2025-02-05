class Bro:
    def __init__(self, message):
        self.name = message

    def getString(self):
        self.name = input("Enter enter a message: ")

    def printString(self):
        print(self.name.upper())

b1 = Bro("")
b1.getString()
b1.printString()