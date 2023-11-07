


class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

# make deposit 
    def deposit(self, amount):
        self.balance += amount
        return self

# make withdraw 
    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

# display account info
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

# yeild_interest function
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


Moneem = BankAccount(0.01,10000)
Kamel = BankAccount(0.01,5000)

Moneem.deposit(800).deposit(1000).deposit(500).withdraw(700).yeild_interest().display_account_info()
Kamel.deposit(1000).deposit(600).deposit(200).withdraw(900).yeild_interest().display_account_info()

BankAccount.print_all_accounts()