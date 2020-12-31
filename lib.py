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

    time = time.monotonic()
    position = 0
    velocity = 0
    acceleration = 0

    times = []
    positions = []
    velocities = []
    accelerations = []

    def __init__(self):
        self.time = time.monotonic()

    def clear(self):
        if self.dimension == 1:
            self.time = time.monotonic()
            self.position, self.velocity, self.acceleartion  = 0, 0, 0
            self.times, self.positions, self.velocities, self.accelerations = [], [], [], []

    def calculate(self):
        pass

    def update(self, position=self.position, velocity=self.velocity, acceleration=self.acceleration):
        pass

