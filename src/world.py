import random as rnd

from pygame import Rect

import items
import maps
from ant import Ant
from wall import Wall


class World():
    """ A world contains all the objects. """

    def __init__(self, screen_size):
        """ Init. """
        self.screen_size = screen_size
        self.bg_color = (100, 100, 100)
        self.ants = []
        self.items = []
        self.walls = []

    def generate(self):
        print('generating world')
        #TODO: Load the map here...
        map_data = maps.load_level_file(1)
        self.generate_walls(self.screen_size)
        self.generate_map_objects(map_data)
        self.generate_ants(500)
        self.generate_queens(10)
        return None

    def generate_walls(self, size):
        """ Generate the wall objects, for collision detection. """
        t = 5  # Wall thickness, off screen!
        self.walls = [
            Wall(Rect((-t, -t), (size[0] + 2 * t, t))),  # top
            Wall(Rect((size[0], -t), (t, size[1] + 2 * t))),  # right
            Wall(Rect((-20, size[1]), (size[0] + 2 * t, t))),  # bot
            Wall(Rect((-t, -t), (t, size[1] + 2 * t))),  # left
        ]
        return None

    def generate_map_objects(self, map_data):
        """ Add map object to the world. """
        print(map_data)
        item_data = map_data['items']
        for class_name, coords in item_data.items():
            # Instantiate different classes depending on item name
            obj = getattr(items, class_name.title())(coords) 
            self.items.append(obj)

    def generate_ants(self, ant_count):
        """ Generate normal ants. """
        print('\tgenerating ants')
        for _ in range(ant_count):
            breed = rnd.choice(['black', 'red'])
            x = int(rnd.random() * self.screen_size[0])
            y = int(rnd.random() * self.screen_size[1])
            self.ants.append(Ant((x,y), breed))
        return None

    def generate_queens(self, queen_count):
        """ Generate queen ants. """
        print('\tgenerating queens')
        for _ in range(queen_count):
            x = int(rnd.random() * self.screen_size[0])
            y = int(rnd.random() * self.screen_size[1])
            breed = rnd.choice(['black', 'red'])
            self.ants.append(Ant((x,y), breed, 'queen'))
        return None
        
    def update(self, dt=None):
        """ Update the world and all it's contents. """
        for ant in self.ants:
            ant.update(dt)

    @property
    def objects(self):
        """ Report all our objects. """
        return self.ants + self.items

