class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("User: " + self.name + " Balance: " + str(self.account_balance))
        return self
Irvin = user("Irvin", "irvincampos76@gmail.com")

Irvin.make_deposit(500000).make_withdrawl(100).display_user_balance()