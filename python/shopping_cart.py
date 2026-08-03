class Shopping_cart:
    def __init__(self):
        self.product=["air fryer","video games", "xbox series X", "PS5" ]
        self.cart=[]
        self.order=[]
    
    def add_to_cart(self):
        self.add_product=input("What product would you like to add? (air fryer, video games, xbox series X and PS5) ")
        if self.add_product in self.product:
            self.cart.append(self.add_product)
            print (f"{self.add_product} has been added to cart")
        else:
            print ("Item does not exist")
    
    def checkout(self):
        if not self.cart:
            print ("Cart empty. Add items before checking out")
        else:
            self.order=self.cart.copy()
            self.cart.clear()
            print (f"Order placed: {self.order}")
    
    def view_cart(self):
        print(self.cart)

cart=Shopping_cart()

while True:
    command=input("What do you want to do (add to cart, checkout, save cart, load cart, see cart, exit)? ")
    
    if command=="add to cart":
        cart.add_to_cart()
    
    elif command=="checkout":
        cart.checkout()
    
    elif command=="exit":
        print("See you soon!")
        break
    
    elif command=="see cart":
        cart.view_cart()
    
    else:
        print("Invalid command")
        