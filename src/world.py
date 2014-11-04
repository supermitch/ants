import random as rnd

from src.ant import Ant

class World():
    """ A world contains all the objects. """

    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.bg_color = (100, 100, 100)
        self.ants = []

    def generate(self):
        print('generating world')
        self.generate_ants(200)
        self.generate_queens(2)
        return None

    def generate_ants(self, ant_count):
        print('\tgenerating ants')
        for _ in range(ant_count):
            breed = rnd.choice(['black', 'red'])
            x = int(rnd.random() * self.screen_size[0])
            y = int(rnd.random() * self.screen_size[1])
            self.ants.append(Ant((x,y), breed))
        return None

    def generate_queens(self, queen_count):
        print('\tgenerating queens')
        for _ in range(queen_count):
            x = int(rnd.random() * self.screen_size[0])
            y = int(rnd.random() * self.screen_size[1])
            breed = rnd.choice(['black', 'red'])
            self.ants.append(Ant((x,y), breed, 'queen'))
        return None
        
    def update(self, dt=None):
        print('updating world')
        self.__update_ants(dt)

    def __update_ants(self, dt=None):
        for ant in self.ants:
            ant.update(dt)


