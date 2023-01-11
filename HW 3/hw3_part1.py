'''
Author: Varun Dhir
Date: 2/19/19
purpose: to make change from $1 with given coins with a user input for item cost 
Sample output:
Enter the coin file name => coins_01-03.txt
Enter the item cost in cents (0-100) => 80 

I have the following coins:
[50, 50, 50, 50, 50, 50, 25, 25, 10, 5, 1, 1]
Change from $1.00 is 20 cents
I cannot make change with my current coins.
I need an additional 3 cents.

'''
import hw3_util

file = input("Enter the coin file name => ")
print(file)
cost = input('Enter the item cost in cents (0-100) => ')
print(cost, '\n')
cost = int(cost)
coins = hw3_util.read_change(file)
print("I have the following coins:\n", coins, sep = '')
change = 100 - cost 
print('Change from $1.00 is {:d} cents'.format(change))
#so I go step by step starting from the largest coin value to the lowest
#using a ton of if/ else and min statements, it finds the max between the amount of change that can be made at each steps 
# to lower the total amount of coins given back to the consumer

if change >= 50:
    if coins.count(50) >= 1:
        value= min(coins.count(50), change// 50)
        change = change - value* 50
    else:
        value = 0
    out_50 = '{} Half Dollars, '.format(value)
else:
    out_50 = '0 Half Dollars, '
    
if change >= 25:
    if coins.count(25) >= 1:
        value= min(coins.count(25), change// 25)
        change = change - value* 25
    else:
        value = 0
    out_25 = '{} Quarters, '.format(value)
else:
    out_25 = '0 Quarters, '
        
if change >= 10:
    if coins.count(10) >= 1:
        value= min(coins.count(10), change// 10)
        change = change - value* 10
    else:
        value = 0
    out_10 = '{} Dimes, '.format(value)    
else:
    out_10 = '0 Dimes, '
    
if change >= 5:
    if coins.count(5) >= 1:
        value= min(coins.count(5), change// 5)
        change = change - value* 5
    else:
        value = 0
    out_5 = '{} Nickels, '.format(value)    
else:
    out_5 = '0 Nickels, '
    
if change >= 1:
    if coins.count(1) >= 1:
        value= min(coins.count(1), change// 1)
        change = change - value* 1
    else:
        value = 0
    out_1 = '{} Pennies'.format(value)    
else:
    out_1 = '0 Pennies'
    
if change == 0:
    print('{}{}{}{}{}'.format(out_50,out_25,out_10,out_5,out_1))
else:
    print('I cannot make change with my current coins.')
    print("I need an additional {} cents.".format(change))