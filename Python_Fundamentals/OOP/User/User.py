

class User:
    
    def __init__(self, name):
        self.name = name
        self.amount = 0

# make withdraw
    def make_withdrawl(self,amount):
        self.amount -= amount

# make deposit
    def make_deposit(self, amount):
        self.amount += amount

# display user account
    def display_user_balance(self):
        print("User: {}, Balance:{} ".format(self.name, self.amount))

# transfert money
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


Moneem = User("Moneem")
Kamel = User("Kamel")
Dojo= User("Dojo")

Moneem.make_deposit(800)
Moneem.make_deposit(600)
Moneem.make_deposit(1200)
Moneem.make_withdrawl(1100)
Moneem.display_user_balance()

Kamel.make_deposit(700)
Kamel.make_deposit(1000)
Kamel.make_withdrawl(900)
Kamel.make_withdrawl(200)
Kamel.display_user_balance()

Dojo.make_deposit(12000)
Dojo.make_withdrawl(1000)
Dojo.make_withdrawl(5000)
Dojo.make_withdrawl(1000)
Dojo.display_user_balance()


Dojo.transfer_money(4000, Kamel)








