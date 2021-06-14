class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate= 0.02, balance= 0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    def make_withdrawl(self, amount):
        self.account.withdrawl(amount)
        return self
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: " + str(self.account.balance))

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

Curry = user("Steph Curry", "ChefCurry@GoldenState.com")
Lebron = user("Lebron James", "GoatJames@LA.com")
Kevin = user("Kevin Durant", "KD@Brooklyn.com")

Curry.make_deposit(300).make_deposit(500).make_deposit(700).make_withdrawl(200).display_user_balance()
Lebron.make_deposit(500).make_deposit(600).make_withdrawl(100).make_withdrawl(200).display_user_balance()
Kevin.make_deposit(1000).make_withdrawl(100).make_withdrawl(200).make_withdrawl(300).display_user_balance()

Apple = BankAccount(0.05, 300)
Orange = BankAccount(0.03, 0)

print(Apple.balance)
print(Orange.balance)

Apple.deposit(200).deposit(100).deposit(300).withdrawl(400).yield_interest().display_account_info()
Orange.deposit(1000).deposit(3000).withdrawl(200).withdrawl(100).withdrawl(400).withdrawl(100).yield_interest().display_account_info()