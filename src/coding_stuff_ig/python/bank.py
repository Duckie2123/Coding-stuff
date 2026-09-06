class bank:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount < 0:
                print("Invalid input. Please enter a positive number.")
            else:
                self.balance += amount
                print(f"Deposited: {amount}. New balance: {self.balance}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount < 0:
            print("Invalid input. Please enter a positive number.")
        else:
            self.balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.balance}")
    
    def check_balance(self):
        print(f"Current balance: {self.balance}")


Bank=bank(0)

while True:
    command = input("Enter command (deposit, withdraw, balance, exit): ").lower()
    
    if command == "deposit":
        Bank.deposit()
    elif command == "withdraw":
        Bank.withdraw()
    elif command == "balance":
        Bank.check_balance()
    elif command == "exit":
        break
    else:
        print("Invalid command.")