from Person import *
class Universe (object):
    def __init__(self, name_, rewards_, portals_):
        '''
        initilaizes it, creates unique object
        '''        
        self.name = name_
        self.rewards = rewards_
        self.portals = portals_
    def __str__ (self):
        '''
        makes it a formated string for printing
        '''        
        outstr = 'Universe: {} ({} rewards and {} portals)\nRewards:'.format(self.name, len(self.rewards), len(self.portals))
        if self.rewards == []:
            outstr += '\nNone'
        else:        
            for reward in self.rewards:
                outstr += '\nat ({},{}) for {} points: {}'.format(reward[0], reward[1], reward[2], reward[3])
        outstr += '\nPortals:'
        if self.portals != []:
            for portal in self.portals:
                outstr += '\n{}:({},{}) -> {}:({},{})'.format(self.name, portal[0], portal[1], portal[2],portal[3], portal[4])
        else:
            outstr += '\nNone'
        return outstr
    
    def pick_up (self, reward):
        '''
        If a reward is picked up it removes it from the list of rewards
        '''
        self.rewards.remove(reward)
        
    def collision (self, reward):
        '''
        when 2 charc. collide they each drop a reward, this puts one of them back it is calld
        twice in the people class
        '''
        self.rewards.append(reward)
