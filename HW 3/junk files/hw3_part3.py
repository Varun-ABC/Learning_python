import math
'''
Author: Varun Dhir
Date: 2/19/19
purpose: to calculate long term bear and berry populations as well as tourist reaction to the bear population
sample output:
Number of bears => 5
5
Size of berry area => 200
200
Year      Bears     Berry     Tourists  
1         5         200.0     50000     
2         3         214.1     0         
3         2         259.9     0         
4         2         334.2     0         
5         3         429.7     0         
6         3         521.7     0         
7         4         633.5     40000     
8         4         723.8     40000     
9         4         827.0     40000     
10        5         944.9     50000     

Min:      2         200.0     0         
Max       5         944.9     50000     
'''
def tourist_pop(bears):
    if bears >= 4 and bears <= 10:
        tourists = 10000 * (bears)
    elif bears > 10 and bears <= 15:
        tourists = 100000 + 20000 * (bears-10)
    else:
        tourists= 0
    return max(0,math.trunc(tourists))

def find_next (bears, berries, tourists):
    berries_next = max(0,(berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05))
    bears_next =  max(0, berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1))
    return (bears_next, berries_next)

bears = input('Number of bears => ')
print(bears)
bears = int(bears.strip())
berries = input('Size of berry area => ')
print(berries)
berries = float(berries.strip())

bear_list= []
berry_list = []
tourists_list = []

tourist = tourist_pop(bears)
i = 1
while i <= 10:
    if i == 1:
        bear_list.append(bears)
        berry_list.append(berries)
        tourists_list.append(tourist)
        print("Year      Bears     Berry     Tourists  ")
        print('{:<10}{:<10}{:<10.1f}{:<10}'.format(i,bears,berries, tourist))
        i += 1
    else:
        berries_next = (find_next(bears, berries, tourist)[1])
        bears_next = math.trunc((find_next(bears, berries, tourist)[0]))
        tourist = tourist_pop(bears_next)
        
        berries= berries_next
        bears = bears_next
        print('{:<10}{:<10}{:<10.1f}{:<10}'.format(i,bears,berries, tourist))
        bear_list.append(bears)
        berry_list.append(berries)
        tourists_list.append(tourist)
        i += 1 
print('\nMin:      {:<10}{:<10.1f}{:<10}'.format(min(bear_list),min(berry_list),min(tourists_list)))
print("Max:      {:<10}{:<10.1f}{:<10}".format(max(bear_list),max(berry_list),max(tourists_list)))