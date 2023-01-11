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

new_coins = []

def subtator(change):
    if change >= 50:
        if coins.count(50) >= 1:
            value= min(coins.count(50), change// 50)
            change = change - value* 50
    return value, change
