class bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        self.balance += amount
        print(f"Deposited: {amount}. New balance: {self.balance}")
    
    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")


x=bank(0)

while True:
    command = input("Enter command (deposit, withdraw, balance, exit): ")
    
    if command == "deposit":
        x.deposit()
    elif command == "withdraw":
        x.withdraw()
    elif command == "balance":
        x.check_balance()
    elif command == "exit":
        break
    else:
        print("Invalid command.")