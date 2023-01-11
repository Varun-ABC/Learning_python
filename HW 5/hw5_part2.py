import random as r
'''
Author: Varun Dhir
Date; 3/21/19
Verion: 1
Building off of the functions created in part one of this assignment and the 
move pokemon from hw 3, I am using those to randomly walk around the grid which the user 
generated a side length. There is a probability (user generated) that they will see a pokemon,
if there is a pokemon there, there is a chance it will catch it or miss 
sample out:
Enter the integer grid size => 10
10
Enter a probability (0.0 - 1.0) => .5
.5
Saw a pokemon at turn 2, location (5, 5)
Missed ...
Saw a pokemon at turn 6, location (3, 5)
Missed ...
Saw a pokemon at turn 8, location (3, 5)
Missed ...
Saw a pokemon at turn 11, location (4, 3)
Missed ...
Saw a pokemon at turn 12, location (4, 4)
Caught it!
Saw a pokemon at turn 13, location (4, 5)
Missed ...
Saw a pokemon at turn 14, location (3, 5)
Missed ...
Saw a pokemon at turn 15, location (3, 6)
Missed ...
Saw a pokemon at turn 19, location (3, 8)
Caught it!
Saw a pokemon at turn 20, location (3, 9)
Caught it!
Trainer left the field at turn 20, location (3, 9).
10 pokemon were seen, 3 of which were captured.
'''
def move_trainer():
    '''
    with no inputs, it outputs a random direction from the list of N,W,E,S
    as well as a random float < 1
    sample output=
    ('N',.4343894789375348934)
    '''    
    direc_list = ['N', 'E', 'S', 'W']
    direc = r.choice(direc_list)
    val = r.random()
    return (direc, val)


def throw_pokeball(num_false, num_true):
    '''
    Uses the inputs of how many true and how many false to make a list with that number of true and false values
    and then from that list it returns a random value
    sample output= 
    True
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
    return r.choice(bool_lst)

def move_pokemon(pos,direction):
    '''
    moves the pokemon a 1 step in user specified direction. 
    it  takes the current position, the direction and the amount of steps and returns the postion as a tuple
    sample output is: (30,45)
    '''
    row = pos[0]
    column = pos[1]
    direction = direction.strip().upper()
    if direction == "N":
        row = row - 1
    elif direction == "S":
        row = row + 1
    elif direction == "W":
        column = column- 1
    elif direction == "E":
        column = column + 1
    return (row, column)


def throw_pokeball(num_false, num_true):
    '''
    Uses the inputs of how many true and how many false to make a list with that number of true and false values
    and then from that list it returns a random value
    sample output= 
    True
    '''    
    bool_lst = []
    i = 0
    j = 0
    while i < num_false:
        bool_lst.append(False)
        i += 1
        #keeps appending a false until you have as many in the list that you desire
    while j < num_true:
        bool_lst.append(True)
        j += 1
    return r.choice(bool_lst)

size = input('Enter the integer grid size => ')
print(size)
#size of grid
size = int(size)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
r.seed(size*11)
f = 3
t = 1
pos = (size//2, size//2)
i = 0
win_loss = []
row = pos[0]
col = pos[1]
# initially the position is the middle of the board and there are 3 falses and 1 true 
#those valuses stay out of the loop so they do not refresh causing an infinte loop\

while 0 < row and row < size-1 and 0 < col and col < size-1:
    #that stops it when the trainer runs out of the feild     
    i += 1
    direc_val = move_trainer()
    # setting move trainer to a value means i can use these specific inputs as many times as i need 
    #if not it would've reset when i called it again    
    direc = direc_val[0]
    pos= move_pokemon(pos, direc)
    if direc_val[1] <= prob and  0 < row and row < size-1 and 0 < col and col < size-1:
        print('Saw a pokemon at turn {}, location {}'.format(i, pos))
        t_f = throw_pokeball(f,t)
        if t_f == True:
            print('Caught it!')
            win_loss.append(1)
            t += 1
            #adds one the the value of t so that when it regenerates the the list for true/ false it updates            
            #win loss keeps track of my wins and losses so i know how many times I won and lost            
        else:
            print('Missed ...')
            win_loss.append(0)
    row = pos[0]
    col = pos[1]
    
print('Trainer left the field at turn {}, location {}.'.format(i, pos))
print('{} pokemon were seen, {} of which were captured.'.format(len(win_loss), win_loss.count(1)))