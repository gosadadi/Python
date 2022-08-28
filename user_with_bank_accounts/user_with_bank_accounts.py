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


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_cards_points = 0
        self.account = BankAccount(int_rate=0.03, balance=0)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.balance
        return self

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_info(self):
        print(self.first_name + self.last_name + self.email + str(self.age))

    def enroll(self):
        if (self.is_rewards_member == True):
            print("user are already a member.")
            return False
        else:
            print("enroll the member.")
            return True
        self.gold_cards_points = 200

    def spend_points(self, amount):
        self.amount = 200-amount
        if (self.amount > 0):
            print(f"you still have {self.amount} points")
        else:
            print("you have used all your points")


p1 = User("Gosa", "Dadi", "gos.d.dadi@gmail.com", 32)
print(p1.first_name+" "+p1.last_name + " "+p1.email + " " + str(p1.age))
p1.display_info()
p1.spend_points(50)
p2 = User("John", " Doe", " doe@gmail.com ", 40)
p2.display_info()
p2.enroll()
p1.make_withdrawal(100)
