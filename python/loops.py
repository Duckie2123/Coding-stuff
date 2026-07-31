l1=['I am', 'You are']
l2=['fine', 'healthy', 'geek']

l2_size=len(l2)
for item in l1:
    print('Start outer for loop')
    i=0
    while i<l2_size:
        print(item, l2[i])
        i+=1
    print('end for loop')