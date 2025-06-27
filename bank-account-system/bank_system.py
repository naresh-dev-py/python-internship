class BankAccount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Balance: {self.balance}")

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Balance: {self.balance}")
        else :
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Balance: {self.balance}")

account1 = BankAccount("Naresh")

account1.deposit(500)
account1.withdraw(200)
account1.check_balance()
