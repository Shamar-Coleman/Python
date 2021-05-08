class BankAccount:
    def __init__(self, account_balance=0, int_rate=.03):
        self.account_balance = account_balance
        self.int_rate = int_rate

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self

    def yield_intrest(self):
        self.account_balance += self.int_rate * self.account_balance
        return self


account1 = BankAccount()

account2 = BankAccount(250, .31)

account1.make_deposit(200).make_deposit(500).make_withdrawl(
    150).yield_intrest().display_account_info()

account2.make_deposit(1209).make_deposit(3267).make_withdrawl(547).make_withdrawl(
    568).make_withdrawl(1000).make_withdrawl(990).yield_intrest().display_account_info()