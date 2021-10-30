class User:

    def __init__(self, name): 
        # assign them accordingly 
        self.name = name
        self.amount = 0 
    
    def make_deposit(self, amount):
        self.amount += amount
        return self
        
    
    def make_withdrawl(self, amount ):
        self.amount -= amount
        return self
        
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

dimitri = User('dimitri')
maggie = User('maggie')
tom = User('tom')

dimitri.make_deposit(100).make_deposit(150).make_deposit(150).make_withdrawl(50).display_user_balance()

maggie.make_deposit(100).make_deposit(500).make_withdrawl(75).make_withdrawl(20).display_user_balance()

tom.make_deposit(1000).make_withdrawl(100).make_withdrawl(100).make_withdrawl(50).display_user_balance()

dimitri.transfer_money(500, maggie)
























