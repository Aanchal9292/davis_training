class Atm:
    def __init__(self,balance,pin):
        self.balance = balance
        self.pin = pin
    def check_balance(self):
        print(f"Your current balance : {self.balance}")
    def withdraw(self, amount,pin):
        # check if user has that much balance
        if amount < self.balance:
            print("Not sufficient balance")