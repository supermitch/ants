"""
Classes for items on maps.

"""
import pygame

class Item():
    def __init__(self):
        pass

class Apple():
    def __init__(self, pos):
        self.pos = pos  # Center (x, y) coords
        self.width = 20
        self.height = 20

        self.rect = pygame.Rect(self.pos[0] - self.width/2,
                                self.pos[1] - self.height/2,
                                self.width, self.height)

        self.color = (255, 100, 100)
        self.mass = float('inf')

