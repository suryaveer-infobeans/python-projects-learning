class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,amount):
        if amount < 0:
            raise ValueError("Amount can not be negative")
        self._balance = amount

    @balance.deleter
    def balance(self):
        del self._balance


account = BankAccount("Bob",1000)
print(account.balance)
account.balance = 1500
print(account.balance)

try:
    account.balance = -500
except ValueError as e:
    print(e)

del account.balance
print(account.balance)