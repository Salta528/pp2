class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def check_Balance(self):
        print(f"Balance : {self.balance}")
    def deposit(self, x):
        if x > 0:
            self.balance += x
            return self.balance
        else:
            return False
    def withdraw(self, x):
        if x <= self.balance:
            self.balance -= x
            return self.balance
        else:
            return False
account = Account("Salta", 0)
account.check_Balance()
account.deposit(1000)
account.check_Balance()
account.withdraw(700)
account.check_Balance()

