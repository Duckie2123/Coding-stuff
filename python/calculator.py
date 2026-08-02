from time import sleep

numbers=list(map(int,input('Enter numbers separated by space: ').split()))
total=sum(numbers)
sleep(1.3)
multiplication=int(input('Enter the multiplication factor: '))
multiply=total*multiplication
divide=int(input('Enter the division factor: '))

sleep(1.3)
if divide!=0:
    division=multiply/divide
else:
    print('You cannot do that twin')

subtract=int(input('Enter the subtraction factor: '))
result=multiply-subtract

print(f'sum of numbers: {total}')
print(f'multiply: {multiply}')
print(f'division: {division}')
print(f'result: {result}')
