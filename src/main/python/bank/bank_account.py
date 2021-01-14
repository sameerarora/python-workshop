class BankAccount():
    ''' A simple Bank Account with name and balance'''

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Allows a deposit of amounts greater than zero"""
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid transaction , amount must be greater than 0")

    def withdraw(self, amount):
        """Allows withdrawal from the account"""
        if amount > self.balance:
            print("Insufficient funds!!")
        else:
            self.balance -= amount

    def print_statement(self):
        print(f"Dear {self.name} you have ₹ {self.balance} in your account!!")

    def __str__(self):
        return f"In str method : {self.name} : {self.balance}"

    def __len__(self):
        return len(self.name)

    def __gt__(self, other):
        return self.balance > other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __eq__(self, other):
        return id(self) == id(other)

    def __repr__(self):
        return self.__class__.__name__ + '(' + repr(self.name) + ', ' + repr(self.balance) + ')'


if __name__ == '__main__':
    acc_1 = BankAccount('John Doe', 500)
    acc_2 = acc_1
    acc_3 = acc_1
    print(len(acc_1))

    if acc_2 == acc_3:
        print(f"accounts are equal")
    else:
        print(f"{acc_2.name} has more money")

    print(repr(acc_1))  # BankAccount('John Doe', 500)
    print(help(acc_1.deposit))
    print((help(acc_1)))

    print(acc_1.__dict__)
