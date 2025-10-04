class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

    def __str__(self):
        return f"Insufficient Balance {self.balance} for withdraw of {self.amount}"


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
        if balance < SavingsAccount.minbal:
            raise ValueError('Minbal is not maintained!')

        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Invalid Amount. It must be > 0')
        if self.balance - SavingsAccount.minbal >= amount:
            self.balance -= amount
        else:
           raise InsufficientFundsError(self.balance, amount)

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "Martin", 10000)
a1.deposit(5000)
print(a1.getbalance())
SavingsAccount.setminbal(2000)
try:
    a1.withdraw(-15000)
except Exception as ex:
    print(ex)

print(a1.getbalance())
