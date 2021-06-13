class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawl(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: ", (self.balance))
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.int_rate * self.balance
            return self

Apple = BankAccount(0.05, 300)
Orange = BankAccount(0.03, 0)
print(Apple.balance)
print(Orange.balance)

Apple.deposit(200).deposit(100).deposit(300).withdrawl(400).yield_interest().display_account_info()
Orange.deposit(1000).deposit(3000).withdrawl(200).withdrawl(100).withdrawl(400).withdrawl(100).yield_interest().display_account_info()