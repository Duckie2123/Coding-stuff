from random import randint
from time import sleep

class hotdog_stand:
    def __init__(self):
        self.hotdog_cost = 4
        self.hotdog_price = 9
        self.total_revenue = 0
        self.total_revenue_lost = 0

    def sell(self):
        self.total_revenue_day = 0
        self.total_revenue_lost_day = 0
        self.overflow_customers = 0

        hotdogs_number = randint(20,51)
        customers_number = randint(10,80)

        if customers_number>hotdogs_number:
            self.overflow_customers=customers_number-hotdogs_number
            self.total_revenue_day+=(customers_number-self.overflow_customers)*(self.hotdog_price-self.hotdog_cost)
            self.total_revenue+=self.total_revenue_day
            self.total_revenue_lost_day=self.overflow_customers*(self.hotdog_price-self.hotdog_cost)
            self.total_revenue_lost+=self.total_revenue_lost_day
            print(f"You lost ${self.total_revenue_lost_day} due to overflow customers. You can always try again tomorrow... But you've made ${self.total_revenue_day}!\n")
            sleep(1)

        elif customers_number<hotdogs_number:
            self.total_revenue_day=customers_number*(self.hotdog_price-self.hotdog_cost)
            self.total_revenue+=self.total_revenue_day
            print(f"You've made ${self.total_revenue_day}!\n")
            print(f"Your total revenue is ${self.total_revenue}\n")
            sleep(1)

        elif customers_number==hotdogs_number:
            self.total_revenue_day=customers_number*(self.hotdog_price-self.hotdog_cost)
            self.total_revenue+=self.total_revenue_day
            print(f"You've made ${self.total_revenue_day}!\n")
            print(f"Your total revenue is ${self.total_revenue}\n")
            sleep(1)

    def weekly_revenue(self):
        return self.total_revenue

    def get_total_revenue_lost(self):
        return self.total_revenue_lost

Hotdog_Stand = hotdog_stand()

for i in range(7):
    Hotdog_Stand.sell()
    print(f"Your total revenue for day {i+1} is ${Hotdog_Stand.total_revenue_day}\n")
    print(f"Your total revenue lost for day {i+1} is ${Hotdog_Stand.total_revenue_lost_day}\n")
    sleep(1)

    if i == 6:
        print(f"Your total revenue for the week is ${Hotdog_Stand.weekly_revenue()}\n")
        print(f"Your total revenue lost for the week is ${Hotdog_Stand.get_total_revenue_lost()}\n")