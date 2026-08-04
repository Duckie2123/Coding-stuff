import pickle
import time

class Dog:
    def __init__(self, name, age): #takes name and age as parameters,makes hunger level 0 and checks the last time the dog was fed
        self.name = name
        self.age = age
        self.hunger_level=0
        self.last_aged = time.time()
        self.last_feed = time.time()

    def details(self): #prints the details of the dog
        print(f"Dog's name: {self.name}")
        print(f"Dog's hunger level: {self.hunger_level}")

    def update(self):
        time.sleep(0.1) # Sleep for 0.1 to avoid high CPU usage
        current_time = time.time()  
        if current_time - self.last_feed >= 5:
            self.hunger_level += 1
            self.last_feed = current_time
            print(f"{self.name}'s hunger is now {self.hunger_level}")
            if self.hunger_level >= 5:
                print(f"{self.name} is too hungry!")

    def feed(self, food):# feeds the dog and resets the hunger level to 0
        self.hunger_level=0
        self.last_feed = time.time()
        print(f"{self.name} has been fed {food}. Hunger level reset to 0.")
    
    def aged(self):#ages the dog by 1 year 
        if time.time() - self.last_aged >= 10: #ages the dog every 10 seconds
            self.age += 1
            self.last_aged = time.time()
        print(f"Dog's age: {self.age}")
        






x=Dog("Buddy",0)



while True: #checks if the dog is hungry every 5 seconds and prompts the user to feed the dog or check its stats
    x.update()
    
    
    command = input("> ")

    if command == "feed":
        x.feed("dog food")

    elif command == "stats":
        x.details()
        x.aged()
        
    elif command == "exit":
        break
    
    elif command == "save":
        with open("dog.pkl", "wb") as f:
            pickle.dump(x, f)
        print("Dog's state saved.")
    
    elif command == "load":
        with open("dog.pkl", "rb") as f:
            x = pickle.load(f)
        print("Dog's state loaded.")
    
    else:
        print("Invalid command. Please enter 'feed', 'stats', 'exit', 'save', 'load', or 'exit'.")






