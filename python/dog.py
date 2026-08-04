import pickle
import time
import threading

class Dog:
    def __init__(self, name, age): #takes name and age as parameters,makes hunger level 0 and checks the last time the dog was fed
        self.name = name
        self.age = age
        self.hunger_level=0
        self.last_aged = time.time()
        self.last_feed = time.time()

    def details(self): #prints the details of the dog
        print(f"\nDog's name: {self.name}")
        print(f"Dog's hunger level: {self.hunger_level}")
        print(f"Dog's age: {self.age}")

    def update(self):
        while True:
            time.sleep(1)
            current_time = time.time()  
            if current_time - self.last_feed >= 5:
                self.hunger_level += 1
                self.last_feed = current_time
                print(f"\n{self.name}'s hunger is now {self.hunger_level}")
                if self.hunger_level >= 5:
                    print(f"{self.name} is too hungry!")

    def feed(self, food):# feeds the dog and resets the hunger level to 0
        self.hunger_level=0
        self.last_feed = time.time()
        print(f"{self.name} has been fed {food}. Hunger level reset to 0.")
    
    def aged(self):#ages the dog by 1 year 
        while True:
            time.sleep(1)
            if time.time() - self.last_aged >= 10: #ages the dog every 10 seconds
                self.age += 1
                self.last_aged = time.time()
                print(f"\n{self.name} is now {self.age} years old")
        

x=Dog("Buddy",0)

thread = threading.Thread(target=x.update,daemon=True)
thread_2 = threading.Thread(target=x.aged, daemon=True)
thread.start()
thread_2.start()

while True: #checks if the dog is hungry every 5 seconds and prompts the user to feed the dog or check its stats
    command = input("> ")

    if command == "feed":
        x.feed("dog food")

    elif command == "stats":
        x.details()
        
    elif command == "exit":
        break
    
    elif command == "save":
        with open("dog.pkl", "wb") as f:
            pickle.dump(x, f)
        print("Dog's state saved.")
    
    elif command == "load":
        try:
            with open("dog.pkl", "rb") as f:
                loaded_dog = pickle.load(f)
                x.__dict__.update(loaded_dog.__dict__)
            print("Dog's state loaded.")
        except FileNotFoundError:
            print("No save file found!")
    
    else:
        print("Invalid command. Please enter 'feed', 'stats', 'exit', 'save', 'load', or 'exit'.")