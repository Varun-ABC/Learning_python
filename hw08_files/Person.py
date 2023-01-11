from Universe import *
'''
author: varun Dhir
purpose create a Person class and functions that help moving and checking stuff
no output
'''
class Person(object):
    def __init__(self, name_, radius_, home_uni_, x_, y_, dx_, dy_, curr_uni_, rewards_= []):
        '''
        initilaizes it, creates unique object
        '''
        self.name = name_
        self.radius = radius_
        self.home_uni = home_uni_
        #home universe is the starting universe
        self.x = x_
        self.y= y_
        self.dx = dx_
        self.dy = dy_
        self.curr_uni = curr_uni_
        self.rewards = rewards_
        if self.rewards == []:
            self.points = 0
            #since all charecters start off with no rewards self.points 
            #will be 0 at first but then it will be added to when points are added
    def __str__ (self):
        '''
        makes it a formated string for printing
        '''
        dx_ = self.dx
        dy_ = self.dy
        outstr = '{} of {} in universe {}\n\tat ({:.1f},{:.1f}) speed ({:.1f},{:.1f}) with {} rewards and {} points'.\
            format(self.name, self.home_uni, self.curr_uni, self.x, self.y, dx_, dy_, len(self.rewards), self.points)
        return outstr
    def move(self):
        '''
        moves the object
        '''
        self.y += self.dy
        self.x += self.dx
    def reward_find (self, loc2):
        '''
        Simple distance formula
        '''
        if ((self.x-loc2[0])**2 + (self.y-loc2[1])**2)**(1/2) <= self.radius:
            return True
        return False
    
    def collision_find (self,other):
        '''
        Simple distance formula but with added radius
        '''        
        if ((self.x-other.x)**2 + (self.y-other.y)**2)**(1/2) <= self.radius+ other.radius:
            return True
        return False        
    def pick_up (self, reward):
        '''
        if a reward is seen they should pick it up, slow down, and gain points
        '''
        self.rewards.append(reward)
        self.n = len(self.rewards)
        self.dx -= (self.n% 2) * (self.n/ 6) * self.dx
        self.dy -= ((self.n+ 1) % 2) * (self.n/6) * self.dy
        self.dx = self.dx
        self.dy = self.dy
        self.points += reward[2]
        #the removal is taken care of in the universe class
    def stop (self):
        '''
        makes sure the object is moving fast enough
        '''
        if abs(self.dy) < 10 or abs(self.dx) < 10:
            return True
    def past_border(self):
        '''
        makes sure the object is on the board
        '''
        if self.x >= 1000 or self.y >= 1000 or self.x <= 0 or self.y <= 0:
            return True
    def collision (self, other, curr_uni, dict_):
        '''
        if they collide they should lose a reward, speed up, and change direction 
        '''
        # I want to return the rewards they drop w/o doing the following calc twice
        outstr = ''
        #reward = List with 4 values: x, y, points, description
        if self.rewards != []:
            x1 = self.rewards.pop(0)
            Universe.collision(curr_uni, x1)
            outstr += '{} dropped "{}", reward returned to {} at\n\t({},{})'.\
                format(self.name, x1[3], x1[4], x1[0], x1[1])
            self.points -= x1[2]
            self.n = len(self.rewards)
            self.dx = -(self.dx + (self.n% 2) * (self.n/ 6) * self.dx)
            self.dy = -(self.dy + ((self.n+ 1) % 2)* (self.n/ 6) * self.dy)
            dict_.append(x1)
        if other.rewards != []:
            other.n = len(other.rewards)
            x2 = other.rewards.pop(0)
            Universe.collision(curr_uni, x2)
            dict_.append(x2)
            if outstr == '':
                outstr += '{} dropped "{}", reward returned to {} at\n\t({},{})'\
                    .format(other.name, x2[3], x2[4], x2[0], x2[1])
            else:
                outstr += '\n{} dropped "{}", reward returned to {} at\n\t({},{})'\
                    .format(self.name, x2[3], x2[4], x2[0], x2[1])
            other.dx = -(other.dx + (other.n% 2) * (other.n/ 6) * other.dx)
            other.dy = -(other.dy + ((other.n+ 1) % 2)* (other.n/ 6) * other.dy)                 
            other.points -= x2[2]
            
        return outstr
    def portal(self, end_uni, ex, ey):
        '''
        Teleportaion between univeses in 3 lines
        '''
        self.curr_uni = end_uni
        self.x = ex
        self.y = ey