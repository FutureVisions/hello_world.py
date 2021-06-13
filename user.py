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
        print("User: " + self.name + ", Balance:" + str(self.account_balance))
Curry = user("Steph Curry", "ChefCurry@GoldenState.com")
Lebron = user("Lebron James", "GoatJames@LA.com")
Kevin = user("Kevin Durant", "KD@Brooklyn.com")

Curry.make_deposit(300).make_deposit(500).make_deposit(700).make_withdrawl(200).display_user_balance()
Lebron.make_deposit(500).make_deposit(600).make_withdrawl(100).make_withdrawl(200).display_user_balance()
Kevin.make_deposit(1000).make_withdrawl(100).make_withdrawl(200).make_withdrawl(300).display_user_balance()
