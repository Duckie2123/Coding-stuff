import random
from time import sleep

revenue_day=0
revenue_lost=0
revenue_week=0
revenue_lost_week=0
revenue_everything=0
revenue_everything_loss=0
hotdogs_bought=0


def hotdogs():
    global revenue_day, revenue_lost, revenue_week, revenue_lost_week, revenue_everything, revenue_everything_loss
    hotdogs_available=[]
    hotdogs_random=random.randint(1,51)
    hotdogs_available.append(hotdogs_random)
    hotdog_cost=2
    hotdog_price=4
    customers=[]
    customers_random=random.randint(1, 101)
    customers.append(customers_random)
    overflow_customers=0
    if customers[0]>hotdogs_available[0]:
        revenue_day=hotdogs_available[0]*(hotdog_price-hotdog_cost)
        print(f"You made ${revenue_day} in revenue but...")
        sleep(1.3)
        overflow_customers=customers[0]-hotdogs_available[0]
        revenue_lost=overflow_customers*(hotdog_price-hotdog_cost)
        revenue_lost_week+=revenue_lost
        revenue_everything_loss+=revenue_lost_week
        revenue_week+=revenue_day
        revenue_everything+=revenue_week
        print(f"You lost {overflow_customers} customers and ${revenue_lost} in revenue. Let's push to the end of the week...")
        sleep(1.3)
    elif customers[0]<hotdogs_available[0]:
        revenue_day=hotdogs_available[0]*(hotdog_price-hotdog_cost)
        revenue_week+=revenue_day
        revenue_everything+=revenue_week
        revenue_lost=overflow_customers*(hotdog_price-hotdog_cost)
        revenue_lost_week+=revenue_lost
        revenue_everything_loss+=revenue_lost_week
        sleep(1.3)
        print(f"YAY! You made ${revenue_day} in revenue without losing money. Lets do this  again for the entire week to get more money:3")
        sleep(1.3)

        
for i in range(1,8):
    hotdogs()


sleep(1.3)
if revenue_week>revenue_lost_week:
    print(f"We're done for the week:D We made ${revenue_week} and lost ${revenue_lost_week}. Subtracting the losses we made ${revenue_everything}")
else:
    revenue_everything_loss=revenue_lost_week-revenue_week
    print(f"Awh3: We did'nt make any money... We lost ${revenue_everything_loss}")