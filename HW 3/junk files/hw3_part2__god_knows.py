'''
Author: Varun Dhir
Date: 2/19/19
purpose: to simulate the movements of a pokemon, including encountering another pokemon
and wining (advancing) or losing (running back)
Sample output:
How many turns? => 10
What is the name of your pikachu? => Piki
How often do we see a Pokemon (turns)? => 2 

Starting simulation, turn 1 Piki at (75, 75)
What direction does Piki walk? => n
What direction does Piki walk? => N
Turn 2, Piki at (65, 75)
What type of pokemon do you meet (W)ater, (G)round? => w
Piki wins and moves to (64, 75)
What direction does Piki walk? => E
What direction does Piki walk? => e
Turn 4, Piki at (64, 85)
What type of pokemon do you meet (W)ater, (G)round? => G
Piki runs away to (64, 75)
What direction does Piki walk? => w
What direction does Piki walk? => W
Turn 6, Piki at (64, 65)
What type of pokemon do you meet (W)ater, (G)round? => r
What direction does Piki walk? => S
What direction does Piki walk? => s
Turn 8, Piki at (74, 65)
What type of pokemon do you meet (W)ater, (G)round? => g
Piki runs away to (64, 65)
What direction does Piki walk? => f
What direction does Piki walk? => w
Turn 10, Piki at (64, 60)
What type of pokemon do you meet (W)ater, (G)round? => W
Piki wins and moves to (64, 59)
Piki ends up at (64, 59), Record: ['Win', 'Lose', 'No Pokemon', 'Lose', 'Win']
'''

turns = input('How many turns? => ')
print (turns)
turns = int(turns)
name = input('What is the name of your pikachu? => ')
print(name)
often = input('How often do we see a Pokemon (turns)? => ')
print(often, "\n")
often = int(often)
i = 1
pos = (75,75)

def move_pokemon(pos,direction,steps):
    #moves the pokemon a 5 steps in user specified direction. 
    row = pos[0]
    column = pos[1]
    direction = direction.strip().upper()
    if direction == "N":
        if row - steps <= 0:
            row = 0
            #if the move will cause it to cross the fence this will stop it at 0
        else:
            row = row - steps
    elif direction == "S":
        if row + steps >= 150:
            row = 150
        else:
            row = row + steps
    elif direction == "W":
        if column - steps <= 0:
            column = 0
        else:
            column = column- steps
    elif direction == "E":
        if column + steps >= 150:
            column = 150
        else:
            column = column + steps
    return (row, column)

if often <= 0:
    poke_list = []
    #if the often is less than or equal to 0 it will use an empty list since range can't incriment by 0
else:
    poke_list= list(range(often, turns+1, often)) 

position = move_pokemon((75,75),'N', 0)
win_loss = []
#list to print out at the end
print('Starting simulation, turn 1 {} at (75, 75)'.format(name))
while i <= turns:
    x = input('What direction does {} walk? => '.format(name))
    print(x)
    x = x.upper()
    if x == 'N' or x == 'S' or x == 'E' or x == 'W':
        position= move_pokemon(position, x, 5)
        last_direction = x + " "
    #else:
        ##even if the pokemon isn't moving in NSEW it still counts as a turn
        #i+= 1        
    if i in poke_list:
        print("Turn {}, {} at {}".format((i),name, position))
        poke_type = input ("What type of pokemon do you meet (W)ater, (G)round? => ")
        print(poke_type)
        poke_type = poke_type.upper()
        if poke_type == 'W':
        #for water type pokemon, the pokemon will win and move up
            position = move_pokemon(position, max("", last_direction), 1)
            print("{} wins and moves to {}".format(name, position))
            win_loss.append('Win')
        elif poke_type == 'G':
                #for ground type, the pokemon will lose and move backward
            position = move_pokemon(position, max("", last_direction), -10)
            print("{} runs away to {}".format(name, position))
            win_loss.append('Lose')
        else:
            win_loss.append('No Pokemon')
        i += 1

print('{} ends up at {}, Record: {}'.format(name, position, win_loss))