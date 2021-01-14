from bank.bank_account import BankAccount


class CheckingsAccount(BankAccount):

    def __init__(self, name, balance, min_balance):
        super(CheckingsAccount, self).__init__(name, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            print(f"Invalid transaction , you need atleast ₹ {self.min_balance} in your checkings account!!!")
        else:
            super(CheckingsAccount, self).withdraw(amount)

    @classmethod
    def foo(cls):
        print(" I am a class level method")


checkings_acc = CheckingsAccount('John Doe', 1000, 500)

checkings_acc.withdraw(600)

CheckingsAccount.foo()
