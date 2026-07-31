money_gained=int(input('amount of money gained from bets:'))
money_lost=int(input('amount of money lost from bets:'))
net_profit=money_gained-money_lost
print('you won $',money_gained)
print('you lost $',money_lost)
if net_profit>0:
    print('maybe this is working after all')
    print('btw you made $',net_profit,',good boy')
elif net_profit<-500:
    print('you are in deep shit nigga. Kill yourself')
    print('btw you lost $',-net_profit,)
else:
    print('maybe this is not working after all. I suggest getting a job')
    print('btw you lost $',-net_profit,)
