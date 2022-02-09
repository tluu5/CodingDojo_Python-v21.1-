class User:
    def _init_(self, name):
        self.name = name
        self.amount = 0
    def make_deposit(self, amount):
        self.amount += amount
    def make_withdrawl(self, amount):
        self.amount -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
Maggie = User("Maggie")
Brian = User("Brian")
Jeff = User("Jeff")
Maggie.make_deposit(100)
Maggie.make_deposit(200)
Maggie.make_deposit(50)
Maggie.make_withdrawl(45)
Maggie.display_user_balance()

Brian.make_deposit(1000)
Brian.make_deposit(1000)
Brian.make_withdrawl(500)
Brian.make_withdrawl(300)
Brian.display_user_balance()

Jeff.make_deposit(1500)
Jeff.make_withdrawl(1000)
Jeff.make_withdrawl(5000)
Jeff.make_withdrawl(3000)
Jeff.display_user_balance()

Brian.transfer_money(400, Maggie)