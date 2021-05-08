class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def tranfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount


shamar = User("Shamar", "shamar@net.com")
brittney = User("Brittney", "Brit@net.com")
ty = User("Ty", "ty@net.com")

shamar.make_deposit(1600).make_deposit(451).make_deposit(278).make_withdrawl(1890).account_balance

brittney.make_deposit(20000).make_deposit(452).make_withdrawl(2784).make_withdrawl(762).account_balance

ty.make_deposit(10000).make_withdrawl(925).make_withdrawl(707).make_withdrawl(345).account_balance

shamar.make_deposit(2000)
shamar.tranfer_money(brittney, 270)
print(shamar.account_balance)
print(brittney.account_balance)