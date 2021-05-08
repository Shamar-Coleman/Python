class User:

    def __init__(self, name, email_address, account):
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.03, account_balance=0)

class BankAccount:

    def __init__(self, int_rate=0.03, account_balance=0, ):
        # self.name = name
        self.account_balance = account_balance
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def tranfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self

    def yield_intrest(self):
        self.account_balance += self.int_rate * self.account_balance
        return self


shamar = User("Shamar", "shamar@net.com", BankAccount())

shamar.account.make_deposit(625).make_withdrawl(
    100).yield_intrest().display_account_info()