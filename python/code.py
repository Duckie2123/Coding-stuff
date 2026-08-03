class code:
    def __init__(self, name, login):
        self.login=login
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}!"
    
    def code(self):
        login=input("Enter your login code: ")
        if login == self.login:
            return "Welcome back!"
        else:
            return "Wrong password. Try again."
    
    def logout(self):
        return "You have been logged out."

y=code("Bleh", "5690")

while True:
    command = input("> ")
    
    if command == "greet":
        print(y.greet())
    elif command == "code":
        print(y.code())
    elif command == "logout":
        print(y.logout())
        break

    else:
        print("Invalid command.")