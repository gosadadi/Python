class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
        else:
            self.balance-5
            print("insufficient funds:chargine a $5 fee")
        return self

    def display_account_info(self):
        print("the balance is:"+str(self.balance))
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance = self.balance + (self.balance*self.int_rate)
        return self


account1 = BankAccount(0.05, 25000)
account2 = BankAccount(0.5, 1000)
account1.deposit(2000).deposit(1000).deposit(5000).withdraw(
    5000).yield_interest().display_account_info()
account2.deposit(100).deposit(200).deposit(100).deposit(
    100).withdraw(500).yield_interest().display_account_info()
