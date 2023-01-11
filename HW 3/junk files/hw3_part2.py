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
    row = pos[0]
    column = pos[1]
    direction = direction.strip().upper()
    if direction == "N":
        if row - steps <= 0:
            row = 0
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
else:
    poke_list= list(range(often, turns+1, often)) 

position = move_pokemon((75,75),'N', 0)
win_loss = []
if turns <= 0:
    pass
else:
    print('Starting simulation, turn 1 {} at (75, 75)'.format(name))
while i <= turns:
    x = input('What direction does {} walk? => '.format(name))
    print(x)
    x = x.upper()
    if x == 'N' or x == 'S' or x == 'E' or x == 'W':
        position= move_pokemon(position, x, 5)
        last_direction = x + " "
        if i in poke_list:
            print("Turn {}, {} at {}".format((i),name, position))
            poke_type = input ("What type of pokemon do you meet (W)ater, (G)round? => ")
            print(poke_type)
            poke_type = poke_type.upper()
            if poke_type == 'W':
            #for water type pokemon
                position = move_pokemon(position, max("", last_direction), 1)
                print("{} wins and moves to {}".format(name, position))
                win_loss.append('Win')
            elif poke_type == 'G':
                position = move_pokemon(position, max("", last_direction), -10)
                print("{} runs away to {}".format(name, position))
                win_loss.append('Lose')
            else:
                win_loss.append('No Pokemon')
        i += 1
    else:
        i+= 1
print('{} ends up at {}, Record: {}'.format(name, position, win_loss))