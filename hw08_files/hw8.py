from Person import *
from Universe import *
import json
'''
Input file => test2.txt
text2.txt

All universes
----------------------------------------
Universe: IntersectionalCS1 (5 rewards and 0 portals)
Rewards:
at (80,80) for 10 points: instant set knowledge
at (33,145) for 40 points: bonus 5 points on one homework
at (270,330) for 30 points: instant knowledge of list comprehension
at (512,271) for 50 points: good variable name generation ability
at (80,190) for 20 points: match of one test case on Submitty
Portals:
None

All individuals
----------------------------------------
Scientist of IntersectionalCS1 in universe IntersectionalCS1
	at (40.0,30.0) speed (20.0,30.0) with 0 rewards and 0 points
Archie of IntersectionalCS1 in universe IntersectionalCS1
	at (220.0,300.0) speed (-20.0,-15.0) with 0 rewards and 0 points
Engineer of IntersectionalCS1 in universe IntersectionalCS1
	at (900.0,800.0) speed (-15.0,-20.0) with 0 rewards and 0 points

Start simulation
----------------------------------------
Scientist picked up "instant set knowledge" at simulation step 1
Scientist of IntersectionalCS1 in universe IntersectionalCS1
	at (60.0,60.0) speed (16.7,30.0) with 1 rewards and 10 points

Scientist and Archie crashed at simulation step 5 in universe IntersectionalCS1
Scientist dropped "instant set knowledge", reward returned to IntersectionalCS1 at
	(80,80)
Scientist of IntersectionalCS1 in universe IntersectionalCS1
	at (126.7,180.0) speed (-16.7,-30.0) with 0 rewards and 0 points 
 Archie of IntersectionalCS1 in universe IntersectionalCS1
	at (120.0,225.0) speed (-20.0,-15.0) with 0 rewards and 0 points 

Archie picked up "match of one test case on Submitty" at simulation step 6
Archie of IntersectionalCS1 in universe IntersectionalCS1
	at (100.0,210.0) speed (-16.7,-15.0) with 1 rewards and 20 points

Scientist picked up "instant set knowledge" at simulation step 8
Scientist of IntersectionalCS1 in universe IntersectionalCS1
	at (76.7,90.0) speed (-13.9,-30.0) with 1 rewards and 10 points

Archie picked up "bonus 5 points on one homework" at simulation step 9
Archie of IntersectionalCS1 in universe IntersectionalCS1
	at (50.0,165.0) speed (-16.7,-10.0) with 2 rewards and 60 points

Scientist stopped at simulation step 11 at location (35.0,0.0)

Archie stopped at simulation step 12 at location (-0.0,135.0)

Engineer picked up "good variable name generation ability" at simulation step 26
Engineer of IntersectionalCS1 in universe IntersectionalCS1
	at (510.0,280.0) speed (-12.5,-20.0) with 1 rewards and 50 points

Engineer stopped at simulation step 40 at location (335.0,0.0)


----------------------------------------
Simulation stopped at step 40
0 individuals still moving
Winners:
Archie of IntersectionalCS1 in universe IntersectionalCS1
	at (-0.0,135.0) speed (-16.7,-10.0) with 2 rewards and 60 points
Rewards:

    match of one test case on Submitty
    bonus 5 points on one homework
'''
#__init__(self, name_, rewards_, portals_)
file = input('Input file => ')
print(file)


data = json.loads(open(file).read())
data =  [{'universe_name': 'IntersectionalCS1', 'rewards': [[80, 80, 10, 'instant set knowledge'], [33, 145, 40, 'bonus 5 points on one homework'], [270, 330, 30, 'instant knowledge of list comprehension'], [512, 271, 50, 'good variable name generation ability'], [80, 190, 20, 'match of one test case on Submitty']], 'portals': [], 'individuals': [['Scientist', 30, 40, 30, 20, 30], ['Archie', 30, 220, 300, -20, -15], ['Engineer', 20, 900, 800, -15, -20]]}]

#data is a list of dictionary
print('All universes')
print('----------------------------------------')
ind_dict= {}
rewards_dict = {}
uni_list = []
portals_dict = {}
for uni in data:
    uni_name = uni['universe_name']
    rewards = uni['rewards']
    portals = uni['portals']
    print(Universe(uni_name,rewards, portals))
    uni_list.append(Universe(uni_name,rewards, portals))
    if uni_name not in ind_dict:
        #created a dictionary with universes as keys and values being 
        #a list of lists that individuals and their info
        ind_dict[uni_name] = []
    ind_dict[uni_name].extend(uni['individuals'])
    if uni_name not in rewards_dict:
        rewards_dict[uni_name] = []
    if uni_name not in portals_dict:
        portals_dict[uni_name] = []    
    rewards_dict[uni_name].extend(rewards)
    portals_dict[uni_name].extend(portals)
    #extend not append b/c portals and rewards are lists
    print()
print('All individuals')
print('----------------------------------------')
people = []
for uni in ind_dict:
    for atri in ind_dict[uni]:
        #print(atri)
        #__init__(self, name_, radius_, home_uni_, x_, y_, dx_, dy_, curr_uni_, rewards_= [])
        name = atri[0]
        rad = atri[1]
        home = uni
        x = atri[2]
        y = atri[3]
        dx = atri[4]
        dy = atri[5]
        curr = uni
        rew = []
        pers = Person(name,rad,home,x,y,dx,dy,curr, rew)
        people.append(pers)
        print(pers) 
people2 = people.copy()
print('\nStart simulation')
print('----------------------------------------')
i = 0
j = 0
first_r = {}
stopped_ppl = []
poop = False
while i < 100:
    if j != 0:
        i += 1
    j = 1
    #essentially just to check initial condtion
    col_list = []
    for pers in people2:
        #needed to use people2 here because i will remove people from people 
        # and when you do that in a for loop it will skip over the next element
        if pers in people:
            #still need to make sure it's still in the correct list
            if Person.stop(pers) == True or Person.past_border(pers) == True:            
                print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'.format(pers.name, i, pers.x, pers.y))
                stopped_ppl.append(pers)
                people.remove(pers)
                continue
            #this moves the person
    if i != 0:
        for pers in people2:
            if pers in people:            
                Person.move(pers)
        for pers in people2:
            if pers in people:            
                for uni in rewards_dict:
                    #this checks if the person finds a reward
                    #for universes in the dictionary of the format {universe name: [reward1, reward2, ...], uni name2: [...]}
                    if uni == pers.curr_uni:
                        #if the universe is the as the person's current universe
                        for r in rewards_dict[uni]:
                            # for reward in the dictionary of rewards
                            if Person.reward_find(pers, (r[0],r[1])):
                                #this means they have found it 
                                #they should pick it up, slow down, and gain points, happens in Person class
                                Person.pick_up(pers,r)
                                for verse in uni_list:
                                    if uni == verse.name:
                                        Universe.pick_up(verse,r) 
                                        rewards_dict[uni].remove(r)
                                        r.append(uni)
                                print('{} picked up "{}" at simulation step {}'.format(pers.name, r[3], i))
                                print(pers)
                                print()                        
                                if Person.stop(pers) == True:
                                    print('{} stopped at simulation step {} at location ({:.1f},{:.1f})'.format(pers.name, i, pers.x, pers.y))
                                    stopped_ppl.append(pers)
                                    people.remove(pers)
                                    continue
        for pers in people2:
            if pers in people:                        
                for pers2 in people2:
                    if pers2 != pers and (pers,pers2) not in col_list:
                        #just makes sure they haven't already bumped into eachother this turn 
                        if Person.collision_find(pers, pers2) == True and pers.curr_uni == pers2.curr_uni:
                            for verse in uni_list:
                                if pers.curr_uni == verse.name:
                                    r_str = Person.collision(pers,pers2, verse, rewards_dict[pers.curr_uni])
                                    print('{} and {} crashed at simulation step {} in universe {}'.format(pers.name, pers2.name, i, pers.curr_uni))
                                    print(r_str)
                                    print(pers, '\n', pers2, '\n')
                                    col_list.append((pers, pers2))
                                    col_list.append((pers2, pers))
        for pers in people2:
            if pers in people:                                            
                for uni in portals_dict:
                    # portals: List of tuples with 5 values: fromx, fromy, to_universe, to_x, to_y
                    for port in portals_dict[uni]:
                        if Person.reward_find (pers, (port[0], port[1])) == True and pers.curr_uni == uni:
                            end_uni = port[2]
                            ex = port[3]
                            ey = port[4]
                            #end points for the portal
                            Person.portal(pers, end_uni, ex, ey)
                            print('{} passed through a portal at simulation step {}'.format(pers.name, i))
                            print(pers, '\n')
        for pers in people2:
            if pers in people:                    
                if (Person.stop(pers) == True or Person.past_border(pers) == True) and pers in people:            
                    print('{} stopped at simulation step {} at location ({:.1f},{:.1f})\n'.format(pers.name, i, pers.x, pers.y))
                    stopped_ppl.append(pers)
                    people.remove(pers)
                    #if they are stopped they will be put into their own list
                    continue
        if len(people) == 0:
            poop = True
            #just a double break
            break
    if poop == True:
        break

print('\n----------------------------------------')
print('Simulation stopped at step {}'.format(i))
outstr = '{} individuals still moving'.format(len(people))
if len(people) > 0:
    str2 = ''
    for peep in people:
        if peep not in stopped_ppl:
            str2 += (peep.name)
    outstr += ': {}'.format(str2)
print(outstr)
print('Winners:')
people3 = []
people.extend(stopped_ppl)
for homie in people:
    for peep in people2:
        if homie.name == peep.name:
            people3.append(homie)


winner_p = 0
winner = []
x = []
for peep in people2:
    tpl = (peep.points, peep)
    x.append(tpl)
x.sort(key = lambda x: x[0], reverse= True)
winner.append(x.pop(0)[1])
for peep in x:
    if peep[1].points == winner[0].points:
        winner.append(peep[1])
        
for win in winner:
    print('{} of {} in universe {}\n\tat ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.\
            format(win.name, win.home_uni, win.curr_uni, win.x, win.y, win.dx, win.dy, len(win.rewards), win.points))
    print('Rewards:')
    print()
    for rew in win.rewards:
        print('   ',rew[-2])
        
        