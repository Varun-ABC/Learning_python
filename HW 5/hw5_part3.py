import random as r
'''
Author: Varun Dhir
Date; 3/21/19
Verion: 1
Builds off of part 2 so that that it runs a simulation for the randomly wandering pokemon trainer 
a user generated number of times
it then outputs the board with which spots had a net caputre or miss number and 
then statistics on what the average number of turns, the min and max amount of turns, and the 
best and worst spots for catches vs misses
sample output:

Enter the integer grid size => 4
4
Enter a probability (0.0 - 1.0) => .7
.7
Enter the number of simulations to run => 33
33

    0   -1   -3    0
    0   -1  -10   -3
    0   -6   -3   -5
    0   -1    0    0
Average number of turns in a simulation was 1.79
Maximum number of turns was 4 in simulation 1
Minimum number of turns was 1 in simulation 3
Best net missed pokemon versus caught pokemon is 0
Worst net missed pokemon versus caught pokemon is -10
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
        #keeps appending a false until you have as many in the list that you desire
    for j in range(num_true):
        bool_lst.append(True)
        j += 1
    return r.choice(bool_lst)

def move_pokemon(pos,direction):
    '''
    moves the pokemon a 1 step in user specified direction. 
    it  takes the current position, the direction and the amount of steps and returns the postion as a tuple
    sample output is: (30,45)
    '''
    size = len(grid)
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


def run_one_simulation(grid, prob):
    '''
    runs the simulation and keeps track of the number of pokemon caught
    on each space in the grid versus the number seen but missed. prob is
    the probability a pokemon will be seen at each turn
    returns the number of turns required to reach the edge of the grid and the new grid
    and the new value for the number of trues in the boolian list and the net win to loss count
    sample output = 
    (5, [[0,2],[1,0]]
    '''
    size = len(grid)
    pos = (size//2, size//2)
    turns = 0
    win_loss = []
    row = pos[0]
    col = pos[1]
    f = 3
    t = 1
    # initially the position is the middle of the board and there are 3 falses and 1 true 
    #those valuses stay out of the loop so they do not refresh causing an infinte loop
    while  0 < row and row < size-1 and 0 < col and col < size-1:
        #that stops it when the trainer runs out of the feild 
        turns += 1
        direc_val = move_trainer()
        # setting move trainer to a value means i can use these specific inputs as many times as i need 
        #if not it would've reset when i called it again
        direc = direc_val[0]
        pos= move_pokemon(pos, direc)
        if direc_val[1] <= prob and  0 < row and row < size-1 and 0 < col and col < size-1:
            t_f = throw_pokeball(f,t)
            if t_f == True:
                win_loss.append(1)
                #win loss keeps track of my wins and losses so i know how many times I won and lost
                grid[pos[0]][pos[1]] += 1
                t += 1
                #adds one the the value of t so that when it regenerates the the list for true/ false it updates
            else:
                win_loss.append(0)
                grid[pos[0]][pos[1]] -= 1
        row = pos[0]
        col = pos[1]
    return (turns, grid)

size = input('Enter the integer grid size => ')
print(size)
size = int(size)
seed_value = 10 * size + size
r.seed(seed_value)
prob = input('Enter a probability (0.0 - 1.0) => ')
print(prob)
prob = float(prob)
sims = input('Enter the number of simulations to run => ')
print(sims)
sims = int(sims)
print('')
t = 1
grid = []
for i in range(size):
    grid.append([0] * (size))

net_list = []
turns = 0
idx = 0

min_turns = 999999999999
#set to an arbritarily high number so that it is overwritten almost immediatly 
max_turns = 0
min_turn_sim = 0
max_turn_sim = 0
while idx != sims:
    idx += 1
    tpl = run_one_simulation(grid, prob)
    #(turns, grid)- the return of run_one_simulation
    if tpl[0] > max_turns:
        max_turns = tpl[0]
        max_turn_sim = idx
        #keeps the max amount of turns only if the value is greater than the current max and the turn that it were iderated on
    if tpl[0] < min_turns:
        min_turns = tpl[0]
        min_turn_sim = idx
        # ditto for min
    turns += tpl[0]
    grid = tpl[1]
for i in grid:
    for j in i:
        print ('{:>5}'.format(j),end = ''.strip())
        net_list.append(j)
    print('')
    #prints me a nice grid

avg_turns = turns / sims
print('Average number of turns in a simulation was {:.2f}'.format(avg_turns))
print('Maximum number of turns was {} in simulation {}'.format(max_turns, max_turn_sim))
print('Minimum number of turns was {} in simulation {}'.format(min_turns, min_turn_sim))
print('Best net missed pokemon versus caught pokemon is {}'.format(max(net_list)))
print('Worst net missed pokemon versus caught pokemon is {}'.format(min(net_list)))