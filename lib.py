import time, threading, logging
import numpy as np
from PIL import Image, ImageGrab
from pynput.keyboard import Key, KeyCode, Controller

logging.basicConfig(
    level=logging.DEBUG,
    filename= 'logging.txt',
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

class PlayerController():
    pass

class ScreenshotManager():
    pass

class FishingController():
    pass

class RoamingController():
    pass

class KineticParticle():
    dimensions = 1
    #calculation range
    average_between = 2

    time = time.monotonic()
    position = 0
    velocity = 0
    acceleration = 0

    times = []
    positions = []
    velocities = []
    accelerations = []

    def __init__(self, name=''):
        self.time = time.monotonic()

    def __getattr__(self, name):
        if name == 'pos':
            return self.position
        elif name == 'vel':
            return self.velocity
        elif name == 'accel':
            return self.acceleration
        elif name in ['vels', 'velocitys']
            return self.velocities
        elif name == 'accels':
            return self.acceleartions

    def valid(self, key, value):
        #validify the value according to its field
        booly = True
        if key in ['pos','position','vel','velocity','accel','acceleration','time', ]:
            booly &= isinstance(value, (int,float))
            if key == 'time':
                booly &= value >= 0
        if key in ['positions','velocities','velocitys','accelerations','times']:
            booly &= isinstance(value, list)
            try:
                booly &= all([isinstance(x, (int,float) for x in value)])
                if key == 'times':
                    booly &= all([x>=0 for x in value])
            except Attribute, ValueError as e:
                return False
        return booly

    def last_value(self, key, amount=1, force=True):
        #get the last 'amount' values for key
        to_return = []
        key += 's'  #plural key
        vals = getattr(self,key)
        for i in range(amount):
            try:
                val = vals[-i]
                to_return.append(val)
            except AttributeError, ValueError as e:
                logging.critical("Cannot get key '{}' at index '{}', {}".format(key,i,e))
                if not force:
                    return []
        return to_return

    def clear(self):
        if self.dimension == 1:
            self.time = time.monotonic()
            self.position, self.velocity, self.acceleartion  = 0, 0, 0
            self.times, self.positions, self.velocities, self.accelerations = [], [], [], []

    def update(self, time=self.time, pos=self.position, vel=self.velocity, accel=self.acceleration):
        #puts active values to stored values. completes any calculations required
        #must have position. for every consecutive field, either get it or calculate
        if self.valid('pos',pos):
            #velocity
            if not self.valid('vel',vel):
                last_pos = self.last_value('vel')
                last_time = self.last_value('time')
                if last_pos and last_time:
                    vel = (pos-last_pos)/(time-last_time)
            if self.valid('vel',vel):
                #acceleration
                if not self.valid('accel',accel):
                    last_vel = self.last_value('accel')
                    last_time = self.last_value('time')
                    if last_vel and last_time:
                        accel = (vel-last_vel)/(time-last_time)
            else:
                logging.critical("Cannot update {} as velocity '{}' is invalid.".format(self.name, vel))
        else:
            logging.critical("Cannot update {} as position '{}' is invalid.".format(self.name, pos))
        #IF ALL VALID, ADD
        if all([self.valid(k,v) for k,v in list(zip(['pos','vel','accel'],[pos,vel,accel])) ]):
            self.positions.append(pos)
            self.velocities.append(vel)
            self.accelerations.append(accel)
        else:
            logging.critical("Could not add active units.".format())
            

