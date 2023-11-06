



class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

# make withdraw
    def make_withdrawl(self,amount):
        self.amount -= amount
        return self

# make deposit
    def make_deposit(self, amount):
        self.amount += amount
        return self

# display user account
    def display_user_balance(self):
        print("{}, Balance:{} ".format(self.name, self.amount))

# transfert money
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


Moneem = User("Moneem")
Kamel = User("Kamel")
Dojo= User("Dojo")


Moneem.make_deposit(800).make_deposit(600).make_deposit(500).make_withdrawl(1100).display_user_balance()

Kamel.make_deposit(1000).make_deposit(700).make_withdrawl(900).make_withdrawl(200).display_user_balance()

Dojo.make_deposit(12000).make_withdrawl(1000).make_withdrawl(5000).make_withdrawl(1000).display_user_balance()



Dojo.transfer_money(2500, Kamel)