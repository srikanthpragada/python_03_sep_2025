class SavingsAccount:
    minbal = 5000

    @staticmethod
    def getminbal():
        return SavingsAccount.minbal

    @staticmethod
    def setminbal(minbal):
        SavingsAccount.minbal = minbal

    def __init__(self, acno, customer, balance):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
            print('Sorry! Insufficient Balance!')

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Martin", 10000)
a1.deposit(5000)
print(a1.getbalance())
SavingsAccount.setminbal(2000)
a1.withdraw(12000)
print(a1.getbalance())
