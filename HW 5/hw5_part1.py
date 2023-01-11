import random as r
'''
Author: Varun Dhir
Date; 3/21/19
Verion: 1
purpose is to define 2 functions and call them a set number of times
also to set a seed from an input
sample output: 
Enter the integer grid size => 10
10
Enter the integer number of Falses => 5
5
Enter the integer number of Trues => 2
2
Setting seed to 110
Directions: ['N', 'E', 'S', 'W']
Selected W, value 0.79
Directions: ['N', 'E', 'S', 'W']
Selected E, value 0.41
Directions: ['N', 'E', 'S', 'W']
Selected S, value 0.64
Directions: ['N', 'E', 'S', 'W']
Selected N, value 0.54
Directions: ['N', 'E', 'S', 'W']
Selected S, value 0.75
Booleans: [False, False, False, False, False, True, True]
Selected False
Booleans: [False, False, False, False, False, True, True]
Selected True
Booleans: [False, False, False, False, False, True, True]
Selected False
Booleans: [False, False, False, False, False, True, True]
Selected False
Booleans: [False, False, False, False, False, True, True]
Selected False
'''
def move_trainer():
    '''
    with no inputs, it outputs a random direction from the list of N,W,E,S
    as well as a random float < 1
    sample output=
    Directions: ['N', 'E', 'S', 'W']
    Selected S, value 0.75
    '''        
    direc = ['N', 'E', 'S', 'W']
    rand = r.choice(direc)
    val = r.random()
    print("Directions: ['N', 'E', 'S', 'W']")
    print('Selected {}, value {:.2f}'.format(rand,val))

def throw_pokeball(num_false, num_true):
    '''
    Uses the inputs of how many true and how many false to make a list with that number of true and false values
    and then from that list it returns a random value
    sample output= 
    Booleans: [False, False, False, False, False, True, True]
    Selected False
    '''
    bool_lst = []
    i = 0
    j = 0
    while i < num_false:
        bool_lst.append(False)
        i += 1
        
    while j < num_true:
        bool_lst.append(True)
        j += 1
    print('Booleans: {}'.format(bool_lst))
    print('Selected {}'.format(r.choice(bool_lst)))


grid = input('Enter the integer grid size => ')
print(grid)
grid = int(grid)
fal = input('Enter the integer number of Falses => ')
print(fal)
fal = int(fal)
tru = input('Enter the integer number of Trues => ')
print(tru)
tru = int(tru)
seed = 11 * grid
print('Setting seed to {}'.format(seed))
r.seed(seed)
#the seed keeps consistant randomly generated numbers

move_trainer()
move_trainer()
move_trainer()
move_trainer()
move_trainer()

throw_pokeball(fal, tru)
throw_pokeball(fal, tru)
throw_pokeball(fal, tru)
throw_pokeball(fal, tru)
throw_pokeball(fal, tru)