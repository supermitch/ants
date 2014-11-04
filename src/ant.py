import math
import random as rnd

from pygame import Rect

class Ant():
    """ An ant. """

    def __init__(self, pos, breed='black', caste='worker'):
        """ Instantiate an ant at position 'pos'. """
        self.breed = breed
        self.caste = caste

        self.pos = pos  # center of the ant

        self.speed = {'black': 40, 'red': 80}[breed]
        self.width = {'black': 10, 'red': 5}[breed]
        self.height = {'black': 4, 'red': 2}[breed]

        if caste == 'queen':
            self.width *= 2.5
            self.height *= 2.5
            self.speed /= 2
 
        self.rect = Rect(self.pos[0] - self.width/2,
                         self.pos[1] + self.height/2,
                         self.width, self.height)

        self.orientation = rnd.uniform(0, 2 * math.pi)  # radians

    def update(self, dt=None):
        self.turn(dt)
        self.move(dt)

    def turn(self, dt=None):
        """ Turn. """
        # TODO: Implement dt
        two_pi = 2 * math.pi
        # We can't turn all the way around in on step
        self.orientation += rnd.uniform(-0.2, 0.2)  # about 10 degrees.
        if self.orientation >= two_pi:
            self.orientation -= two_pi
        if self.orientation < 0:
            self.orientation += two_pi

    def move(self, dt=None):
        """ Move. """
        distance = dt/1000.0 * self.speed if dt else 3
        dx = distance * math.cos(self.orientation)
        dy = distance * math.sin(self.orientation)
        self.pos = (self.pos[0] + dx, self.pos[1] - dy)

