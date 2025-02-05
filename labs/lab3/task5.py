class Account:
    def __init__(self):
        self.owner = input("Enter a name: ")
        self.balance = int(input("Enter a balance: "))  # 50000
        self.pin = int(input("Enter pin: "))

    def deposit(self):
        print(self.balance)

    def withdraw(self):
        pinCode = int(input("Enter pinCode"))
        if pinCode == self.pin:
            drawbalance = int(input("Enter a drawBalance: "))
            if(self.balance - drawbalance >= 0):
                self.balance -= drawbalance
            else:
                print("Недостаточно средств!!!")
        else:
            print("тыдын дын тыдыдындын")

print("Hello, can you enter some info about you?")
a1 = Account()
while(True):
    print("[1] get Total Balance")
    print("[2] withdraw")
    print("[0] exit")
    choice = int(input())
    if choice == 0:
        break
    elif choice == 1:
        a1.deposit()
    elif choice == 2:
        a1.withdraw()