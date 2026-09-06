class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def subtract(self, a, b):
        self.result = a - b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def divide(self, a, b):
        try: 
            self.result = a / b
            return self.result
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

calc = Calculator()

while True:
        operation = input("Enter operation (add, subtract, multiply, divide) or 'exit' to quit: ").lower()
        
        if operation not in ["add", "subtract", "multiply", "divide", "exit"]:
            print("Wrong input. Please enter an operation that is listed in the options. (add, subtract, multiply, divide, exit)")
            continue
        elif operation == "exit":
            break
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter actual numbers.")
            continue
        if operation == "add":
            print(f"Result: {calc.add(num1, num2)}")
        elif operation == "subtract":
            print(f"Result: {calc.subtract(num1, num2)}")
        elif operation == "multiply":
            print(f"Result: {calc.multiply(num1, num2)}")
        elif operation == "divide":
            result = calc.divide(num1, num2)
            if result is not None:
                print(f"Result: {calc.divide_result}")